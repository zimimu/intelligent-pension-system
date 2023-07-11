# -*- coding: utf-8 -*-

"""
训练人脸识别模型
"""


# import the necessary packages
from imutils import paths
from oldcare.facial import FaceUtil

# global variable
dataset_path = 'images'
output_encoding_file_path = 'models/face_recognition_hog.pickle'

# grab the paths to the input images in our dataset
print("[INFO] quantifying faces...")
image_paths = list(paths.list_images(dataset_path))

if len(image_paths) == 0:
    print('[ERROR] no images to train.')
else:
    faceutil = FaceUtil()
    print("[INFO] training face embeddings...")
    faceutil.save_embeddings(image_paths, output_encoding_file_path)
