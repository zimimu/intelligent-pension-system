import cv2
import numpy as np
import os
import time
import subprocess
import argparse
from keras.preprocessing.image import image_utils
from keras.models import load_model


def fire_detection(frame):
    # 全局变量
    model_path = 'caresystem/views/models/fire_detection.hdf5'
    output_fall_path = 'caresystem/views/supervision/firedata'
    TARGET_WIDTH = 48
    TARGET_HEIGHT = 48

    # 加载模型
    model = load_model(model_path)

    # 图像预处理
    roi = cv2.resize(frame, (TARGET_WIDTH, TARGET_HEIGHT))
    roi = roi.astype("float") / 255.0
    roi = image_utils.img_to_array(roi)
    roi = np.expand_dims(roi, axis=0)

    # 检测是否发生火灾
    (fall, normal) = model.predict(roi)[0]
    label = "Fire (%.2f)" % fall if fall > normal else "Normal (%.2f)" % normal

    # 在图像上绘制标签
    cv2.putText(frame, label, (frame.shape[1] - 150, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    # 如果检测到火灾
    if fall > normal:
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        event_desc = '有火灾发生!!!'
        event_location = '房间'
        print('[EVENT] %s, 房间, 有火灾发生!!!' % current_time)
        cv2.imwrite(os.path.join(output_fall_path, 'snapshot_%s.jpg' % (time.strftime('%Y%m%d_%H%M%S'))), frame)

    return frame


# 初始化摄像头
vs = cv2.VideoCapture('input_video.mp4')

# 读取视频帧并进行处理
while True:
    # 读取视频帧
    ret, frame = vs.read()

    # 如果无法读取到帧，则退出循环
    if not ret:
        break

    # 进行火灾检测
    result = fire_detection(frame)

    # 显示结果图像
    cv2.imshow('Fire Detection', result)

    # 按下ESC键退出循环
    if cv2.waitKey(1) == 27:
        break

# 释放摄像头资源
vs.release()

# 关闭所有窗口
cv2.destroyAllWindows()
