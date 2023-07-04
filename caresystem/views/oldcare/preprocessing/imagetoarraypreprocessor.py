# import the necessary packages
# 考虑到有的深度学习框架如Tensorflow，把图像的channel放在最后（高，宽，通道），有的框架如Thearo把图像的channel放在最前（通道，高，宽）。
from keras.preprocessing.image import image_utils

class ImageToArrayPreprocessor:
	def __init__(self, dataFormat=None):
		# store the image data format
		self.dataFormat = dataFormat

	def preprocess(self, image):
		# apply the Keras utility function that correctly rearranges
		# the dimensions of the image
		return image_utils.img_to_array(image, data_format=self.dataFormat)
