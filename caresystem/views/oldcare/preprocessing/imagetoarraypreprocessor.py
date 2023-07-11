# import the necessary packages
from keras.utils import image_utils


class ImageToArrayPreprocessor:
    def __init__(self, dataFormat=None):
        # store the image data format
        self.dataFormat = dataFormat

    def preprocess(self, image):
        # apply the Keras utility function that correctly rearranges
        # the dimensions of the image
        return image_utils.img_to_array(image, data_format=self.dataFormat)
