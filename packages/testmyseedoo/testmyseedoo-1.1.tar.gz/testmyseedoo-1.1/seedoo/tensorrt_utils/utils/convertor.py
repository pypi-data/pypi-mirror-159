import tensorrt as trt
import onnx
from torch import nn
import torch
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
