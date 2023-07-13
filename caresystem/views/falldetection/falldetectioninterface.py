# 导入包
import argparse
from oldcare.facial import FaceUtil
from PIL import Image, ImageDraw, ImageFont
from oldcare.utils import fileassistant
import numpy as np
import time
import cv2
import PoseModule as pm
import math

# 全局变量
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
success = True
bs = 0
ratio = 0
height_all = 0
baseH = 0
point_one=None

def falldetection(success, img):
    global count, dir, pTime,bs, ratio, height_all, baseH, point_one
    if success:
        img = cv2.resize(img, (640, 480))
        imgCanvas = np.zeros((480, 640, 3), np.uint8)
        imgCanvas = detector.findPose(img, imgCanvas, True)
        lmList, bbox = detector.findPosition(img, True)

        if len(lmList) != 0:
            if True:
                # 两髋中心点
                point_hip = detector.midpoint(img, 23, 24, draw=False)
                point_foot = detector.midpoint(img, 29, 30, draw=False)
                point_shouder = detector.midpoint(img, 11, 12, draw=False)
                # 两脚中点

                baseH = (point_hip['y'] - point_foot['y'])
                mark=(point_shouder['y'] - point_hip['y'])
                print(baseH,mark)
                if baseH > -40 :
                    bs = 2
                elif baseH < -40:
                    bs = 0
                    i = 0
            if bs == 2:
                cv2.putText(img, str("fall"), (450, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 0), 5)
        else:
            bs = 0
            i = 0
        print("%.3f" % baseH, bs)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
    return img
