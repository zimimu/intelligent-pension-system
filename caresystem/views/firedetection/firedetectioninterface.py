# -*- coding: utf-8 -*-
"""
摔倒检测模型主程序

用法：
python checkingfalldetection.py
python checkingfalldetection.py --filename tests/firedata.mp4

"""

from keras.preprocessing.image import image_utils
from keras.models import load_model
import numpy as np
import cv2
import os
import time

def fire_detection(frame):
    # 控制陌生人检测
    fall_timing = 0  # 计时开始
    fall_start_time = 0  # 开始时间
    fall_limit_time = 1  # if >= 1 seconds, then he/she falls.

    # 全局变量
    model_path = '../models/fire_detection.hdf5'
    output_fall_path = '../supervision/firedata'
    # your python path
    python_path = '/home/reed/anaconda3/envs/tensorflow/bin/python'

    # 全局常量
    TARGET_WIDTH = 48
    TARGET_HEIGHT = 48

    # 初始化摄像头
    image = frame.copy()

    roi = cv2.resize(image, (TARGET_WIDTH, TARGET_HEIGHT))
    roi = roi.astype("float") / 255.0
    roi = image_utils.img_to_array(roi)
    roi = np.expand_dims(roi, axis=0)

    # 加载模型
    model = load_model(model_path)

    print('[INFO] 开始检测是否发生火灾...')
    # 不断循环
    counter = 0

    # determine facial expression
    (fall, normal) = model.predict(roi)[0]
    label = "Fire (%.2f)" % fall if fall > normal else "Normal (%.2f)" % normal

    # display the label and bounding box rectangle on the output frame
    cv2.putText(image, label, (image.shape[1] - 150, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    if fall > normal:
        if fall_timing == 0:  # just start timing
            fall_timing = 1
            fall_start_time = time.time()
        else:  # already started timing
            fall_end_time = time.time()
            difference = fall_end_time - fall_start_time

            current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

            if difference < fall_limit_time:
                print('[INFO] %s, 走廊, 火焰仅出现 %.1f 秒. 忽略.' % (current_time, difference))
            else:  # strangers appear
                event_desc = '有火灾发生!!!'
                event_location = '房间'
                print('[EVENT] %s, 房间, 有火灾发生!!!' % current_time)
                cv2.imwrite(os.path.join(output_fall_path, 'snapshot_%s.jpg' % (time.strftime('%Y%m%d_%H%M%S'))), image)

    cv2.imshow('Fire detection', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return frame

