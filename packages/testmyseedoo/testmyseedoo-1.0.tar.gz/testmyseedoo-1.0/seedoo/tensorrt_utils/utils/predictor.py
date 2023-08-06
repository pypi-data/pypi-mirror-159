import pandas as pd
import numpy as np
import tensorrt as trt
import pycuda.driver as cuda
import pycuda.autoinit
import cv2
import time
import torch
import torchvision
from torchvision.transforms import (Compose, Resize, PILToTensor)
from PIL import Image
import logging
import os


class Predictor:
    """Predicts boxes on an image with engine and saves a new image with bounding boxes
    Args:
        pth: string with engine path
    Returns:
        None
    """

    def __init__(self, pth: str):
        self.logger = logging.getLogger(__name__)
        self.pth = pth
        self.engine = None
        self._width = None
        self._height = None
        self._pandas_output = None
        self._predictor = None
        self._stream = None
        self._device_input = None
        self._device_output = None
        self._output_shape = None
        self._host_output = None
        self._context = None

    def preprocess_image(self, image):
        """Processes image.
        Args:
            image: a string or an RGB-image
        Returns:
            tensor of shape (b,c,w,h)
        """
        if isinstance(image, str):
            image = Image.open(image)
        # do transformations
        transform = Compose([
            Resize((self._height, self._width)),
            PILToTensor()
        ])
        tensor = transform(image) / 255.
        # adding the first dimenction
        batch_data = torch.unsqueeze(tensor, 0).numpy()
        return batch_data

    def predict(self, image):
        """Predict with engine file
        Args:
            image: string containing a path to image
        Returns:
            Torch tensor with bounding boxes (x,y,w,h) with confidence and class for YOLO_V5
        """
        # engine initializing
        if not self._stream:
            print('Reading engine file...')
            # activating all tensorrt modules
            trt.init_libnvinfer_plugins(None, '')
            logger = trt.Logger(trt.Logger.WARNING)
            # model = self.engine
            self.logger.info('Deserialize engine...')
            with open(self.pth, 'rb') as f, trt.Runtime(logger) as runtime:
                self.engine = runtime.deserialize_cuda_engine(f.read())
            self._context = self.engine.create_execution_context()
            self.logger.info(
                'Get sizes of input and output and allocate memory required for input data and for output data...')
            # get sizes of input and output and allocate memory required for input data and for output data
            for binding in self.engine:
                if self.engine.binding_is_input(binding):  # we expect only one input
                    input_shape = self.engine.get_binding_shape(binding)
                    self._width = input_shape[3]
                    self._height = input_shape[2]
                    input_size = trt.volume(input_shape) * self.engine.max_batch_size * np.dtype(
                        np.float32).itemsize  # in bytes
                    self._device_input = cuda.mem_alloc(input_size)
                else:  # and one output
                    self._output_shape = self.engine.get_binding_shape(binding)
                    self.logger.info(f'output_shape {self._output_shape}')
                    # create page-locked memory buffers (i.e. won't be swapped to disk)
                    self._host_output = cuda.pagelocked_empty(
                        trt.volume(self._output_shape) * self.engine.max_batch_size,
                        dtype=np.float32
                    )
                    self.logger.info(f'host_output {self._host_output.shape}')
                    self._device_output = cuda.mem_alloc(self._host_output.nbytes)
                    self.logger.info(f'device_output {self._device_output}')
            # Create a stream in which to copy inputs/outputs and run inference.
            self._stream = cuda.Stream()
            print('Start prediction..')

        # prediction
        host_input = np.array(self.preprocess_image(image), dtype=np.float32, order='C')
        # print(self._device_input, host_input, self._stream)
        cuda.memcpy_htod_async(self._device_input, host_input, self._stream)
        # run inference
        self._context.execute_async(
            bindings=[int(self._device_input),
                      int(self._device_output)],
            stream_handle=self._stream.handle
        )
        cuda.memcpy_dtoh_async(self._host_output, self._device_output, self._stream)
        self._stream.synchronize()
        self.logger.info(f'host_output: {self._host_output}')
        self.logger.info(f'output_shape: {self._output_shape}')
        # postprocess results
        raw_output = torch.Tensor(self._host_output)
        raw_output = raw_output.reshape(
            self.engine.max_batch_size,
            self._output_shape[1] * self._output_shape[2]
        )
        shaped_output = raw_output.view((1, int(raw_output.size()[1] / 85), 85))
        # nms_output = non_max_suppression(
        #     prediction=shaped_output,
        #     conf_thres=0.25,
        #     iou_thres=0.45
        # )
        # return to_pandas(nms_output)
        return None

# HELPER FUNCTIONS
def to_pandas(output):
    """output: """
    converted_output = pd.DataFrame(
        output[0].tolist(),
        columns=['xmin', 'ymin', 'xmax', 'ymax', 'confidence', 'class']
    )
    return converted_output


def xywh2xyxy(x):
    """Convert nx4 boxes from [x, y, w, h] to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right"""
    y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
    y[:, 0] = x[:, 0] - x[:, 2] / 2  # top left x
    y[:, 1] = x[:, 1] - x[:, 3] / 2  # top left y
    y[:, 2] = x[:, 0] + x[:, 2] / 2  # bottom right x
    y[:, 3] = x[:, 1] + x[:, 3] / 2  # bottom right y
    return y


def non_max_suppression(prediction=None,
                        conf_thres=0.25,
                        iou_thres=0.8,
                        classes=None,
                        agnostic=False,
                        multi_label=False,
                        labels=(),
                        max_det=300):
    """Non-Maximum Suppression (NMS) on inference results to reject overlapping bounding boxes
    Returns:
         list of detections, on (n,6) tensor per image [xyxy, conf, cls]
    """
    bs = prediction.shape[0]  # batch size
    nc = prediction.shape[2] - 5  # number of classes
    xc = prediction[..., 4] > conf_thres  # candidates
    # Checks
    assert 0 <= conf_thres <= 1, f'Invalid Confidence threshold {conf_thres}, valid values are between 0.0 and 1.0'
    assert 0 <= iou_thres <= 1, f'Invalid IoU {iou_thres}, valid values are between 0.0 and 1.0'
    # Settings
    # min_wh = 2  # (pixels) minimum box width and height
    max_wh = 7680  # (pixels) maximum box width and height
    max_nms = 30000  # maximum number of boxes into torchvision.ops.nms()
    time_limit = 0.3 + 0.03 * bs  # seconds to quit after
    redundant = True  # require redundant detections
    multi_label &= nc > 1  # multiple labels per box (adds 0.5ms/img)
    merge = False  # use merge-NMS
    t = time.time()
    output = [torch.zeros((0, 6), device=prediction.device)] * bs
    for xi, x in enumerate(prediction):  # image index, image inference
        # Apply constraints
        # x[((x[..., 2:4] < min_wh) | (x[..., 2:4] > max_wh)).any(1), 4] = 0  # width-height
        x = x[xc[xi]]  # confidence
        # Cat apriori labels if autolabelling
        if labels and len(labels[xi]):
            lb = labels[xi]
            v = torch.zeros((len(lb), nc + 5), device=x.device)
            v[:, :4] = lb[:, 1:5]  # box
            v[:, 4] = 1.0  # conf
            v[range(len(lb)), lb[:, 0].long() + 5] = 1.0  # cls
            x = torch.cat((x, v), 0)
        # If none remain process next image
        if not x.shape[0]:
            continue
        # Compute conf
        x[:, 5:] *= x[:, 4:5]  # conf = obj_conf * cls_conf
        # Box (center x, center y, width, height) to (x1, y1, x2, y2)
        box = xywh2xyxy(x[:, :4])
        # Detections matrix nx6 (xyxy, conf, cls)
        if multi_label:
            i, j = (x[:, 5:] > conf_thres).nonzero(as_tuple=False).T
            x = torch.cat((box[i], x[i, j + 5, None], j[:, None].float()), 1)
        else:  # best class only
            conf, j = x[:, 5:].max(1, keepdim=True)
            x = torch.cat((box, conf, j.float()), 1)[conf.view(-1) > conf_thres]
        # Filter by class
        if classes is not None:
            x = x[(x[:, 5:6] == torch.tensor(classes, device=x.device)).any(1)]
        # Apply finite constraint
        # if not torch.isfinite(x).all():
        #     x = x[torch.isfinite(x).all(1)]
        # Check shape
        n = x.shape[0]  # number of boxes
        if not n:  # no boxes
            continue
        elif n > max_nms:  # excess boxes
            x = x[x[:, 4].argsort(descending=True)[:max_nms]]  # sort by confidence
        # Batched NMS
        c = x[:, 5:6] * (0 if agnostic else max_wh)  # classes
        boxes, scores = x[:, :4] + c, x[:, 4]  # boxes (offset by class), scores
        i = torchvision.ops.nms(boxes, scores, iou_thres)  # NMS
        if i.shape[0] > max_det:  # limit detections
            i = i[:max_det]
        if merge and (1 < n < 3E3):  # Merge NMS (boxes merged using weighted mean)
            # update boxes as boxes(i,4) = weights(i,n) * boxes(n,4)
            iou = box_iou(boxes[i], boxes) > iou_thres  # iou matrix
            weights = iou * scores[None]  # box weights
            x[i, :4] = torch.mm(weights, x[:, :4]).float() / weights.sum(1, keepdim=True)  # merged boxes
            if redundant:
                i = i[iou.sum(1) > 1]  # require redundancy
        output[xi] = x[i]
        if (time.time() - t) > time_limit:
            logging.warning(f'WARNING: NMS time limit {time_limit:.3f}s exceeded')
            break  # time limit exceeded
    return output
