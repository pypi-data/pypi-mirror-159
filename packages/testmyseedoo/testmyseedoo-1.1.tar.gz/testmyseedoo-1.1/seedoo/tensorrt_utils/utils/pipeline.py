import pandas as pd
import numpy as np
import tensorrt as trt
import pycuda.driver as cuda
import cv2
import onnx
from torch import nn
import time
import torch
import torchvision
from torchvision.transforms import (Compose, Resize, ToTensor, PILToTensor)
from PIL import Image
import logging
import os


class Convertor:
    """Class for building engine from torch or onnx model
    Args:
        pth: string contains path to weights for model, onnx model or engine,
        width: int with a desired width for engine input,
        height: int with a desired height for engine input,
        model: object variable with model,
        force: flag allows force conversion and rewriting existing engine file with the same name (default: False).
    Returns:
        convert method returns a string with output engine name.
        """

    def __init__(self, pth=None, width=None, height=None, model=None, force=False):
        self.logger = logging.getLogger(__name__)
        self.model = model
        self.force = force
        self.pth = pth
        self.width = width
        self.height = height
        self._onnx_output_name = os.path.basename(pth).split('.')[0] + '.onnx'
        self._engine_output_name = os.path.basename(pth).split('.')[0] + '.engine'
        self.model = model

    def convert_to_onnx(self):
        # checking if onnx model already exists in current dir
        self.logger.info('Conversion to onnx format..')
        # print('Converting model to ONNX format started...')
        # generate dummy input
        self.logger.info(f"Input image size (WxH):({self.width}x{self.height})")
        dummy_input = torch.Tensor(1, 3, self.height, self.width).cuda()  # (b,c,h,w)
        # set inference mode on cuda
        self.model.eval()
        self.model.cuda()
        output = self.model(dummy_input)
        # convert to onnx and save
        file = os.path.split(self.pth)[0] + '/' + self._engine_output_name
        torch.onnx.export(
            self.model, dummy_input, file, opset_version=12,
            input_names=["input"], output_names=["output"], export_params=True
        )
        # check that the model converted fine
        self.logger.info("Onnx conversion finished. Checking onnx model converted fine...")
        onnx_model = onnx.load(self._onnx_output_name)  # self._onnx_output_name
        onnx.checker.check_model(onnx_model)
        self.logger.info("Model was successfully converted to onnx format!")
        self.logger.info(f"Onnx model was saved to {self._onnx_output_name}")

    def convert_to_engine(self):
        self.logger.info('Building engine from onnx model started...')
        # initialize TensorRT engine and parse ONNX model
        logger = trt.Logger(trt.Logger.INFO)
        builder = trt.Builder(logger)
        # set only one image in batch
        builder.max_batch_size = 1
        # create_network
        explicit_batch = (1 << int(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH))
        network = builder.create_network(explicit_batch)
        parser = trt.OnnxParser(network, logger)
        # check parser errors
        self.logger.info("Checking possible parser's errors...")
        for error in range(parser.num_errors):
            self.logger.info(parser.get_error(error))
        # allow TensorRT to use up to 1GB of GPU memory for tactic selection
        config = builder.create_builder_config()
        config.max_workspace_size = 1 << 30
        config.set_flag(trt.BuilderFlag.FP16)
        # parser.parse() populates the network object with information from the model file
        with open(self.pth, 'rb') as model:
            self.logger.info("Beginning ONNX file parsing...")
            parser.parse(model.read())
        self.logger.info("Completed parsing of onnx file")
        # generate TensorRT engine optimized for the target platform
        self.logger.info('Building and serializing engine...')
        inputs = [network.get_input(i) for i in range(network.num_inputs)]
        outputs = [network.get_output(i) for i in range(network.num_outputs)]
        # engine serializing
        file = os.path.split(self.pth)[0] + '/' + self._engine_output_name
        with builder.build_engine(network, config) as engine, open(file, 'wb') as f:
            f.write(engine.serialize())
        self.logger.info(f"Engine successfully built and saved as {file}.")
        return file

    def name_exists(self, name, force):
        if force or name not in os.listdir(os.path.split(self.pth)[0]):
            return False
        return True

    def convert(self, force=False):
        # check weights file
        assert os.path.isfile(self.pth), f"File does not exist: {self.pth}"

        # object model
        if self.model:
            # file name check
            if self.name_exists(self._onnx_output_name, force):
                self.logger.error("Engine already exists!")
                return os.path.split(self.pth)[0] + '/' + self._engine_output_name
            # validation of the model
            assert isinstance(self.model, nn.Module), "Your model is not valid torch model!"
            # loading weights to the model
            self.model.load_state_dict(torch.load(self.pth))
            self.convert_to_onnx()
            self.convert_to_engine()

        elif isinstance(self.pth, str):
            # onnx model
            if os.path.splitext(self.pth)[1] == '.onnx':
                if self.name_exists(self._engine_output_name, force):
                    self.logger.error("Engine file already exists!")
                    return os.path.split(self.pth)[0] + '/' + self._engine_output_name
                self.convert_to_engine()
            elif os.path.splitext(self.pth)[1] == '.engine':
                self.logger.error("Engine can't be converted! Use the engine with Predictor class!")
                return


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
            import tensorrt as trt
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
        nms_output = non_max_suppression(
            prediction=shaped_output,
            conf_thres=0.25,
            iou_thres=0.45
        )
        return to_pandas(nms_output)


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


def draw_rect(output, img_path, width, height):
    # import matplotlib.pyplot as plt
    # %matplotlib inline
    """Draw recrangles on an image
    Args:
        results from YOLO
    Returns:
        image with rectangles, classs name and confidence in %
    """
    transforms = Compose([
        Resize((height, width)),
        PILToTensor()
    ])
    # read input image
    image = Image.open(img_path)
    # do transformations
    image = transforms(image)
    names = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
             'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
             'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
             'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
             'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
             'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
             'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard',
             'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
             'teddy bear', 'hair drier', 'toothbrush']
    classes = dict()
    for i, name in enumerate(names):
        classes[i] = name
    for row in range(len(output)):
        xmin = output.loc[row][0]  # left highest point
        ymax = output.loc[row][3]  # left highest point
        xmax = output.loc[row][2]  # right lowest point
        ymin = output.loc[row][1]  # right lowest point
        class_name = classes[int(output.loc[row][5])]
        pt1 = (int(xmin), int(ymax))
        pt2 = (int(xmax), int(ymin))
        image = cv2.rectangle(
            image,
            pt1,
            pt2,
            color=(225, 0, 0),
            thickness=2)
        cv2.putText(
            image,
            f"{class_name}: {str(round(output.loc[row][4], 1) * 100)}%",
            (int(xmin), int(ymin) - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )
    save_path = os.getcwd() + "/data/outputs/" + f"{img_path.split('/')[-1]}"
    logging.info(f"Output file path: {save_path}")
    cv2.imwrite(save_path, image)
    # plt.figure(figsize=(10,10))
    # plt.imshow(image)
