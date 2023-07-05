# 导入包
import argparse
from caresystem.views.oldcare.facial import FaceUtil
from PIL import Image, ImageDraw, ImageFont
from caresystem.views.oldcare.utils import fileassistant
import numpy as np
import time
import cv2
import caresystem.views.falldetection.PoseModule as pm
import math

# 全局变量
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
success = True
i = 0
bs = 0
ratio = 0
height_all = 0
baseH = 0
point_one=None

def falldetection(success, img, i):
    global count, dir, pTime,bs, ratio, height_all, baseH, point_one
    if success:
        img = cv2.resize(img, (640, 480))
        imgCanvas = np.zeros((480, 640, 3), np.uint8)
        imgCanvas = detector.findPose(img, imgCanvas, True)
        lmList, bbox = detector.findPosition(img, True)

        if len(lmList) != 0:
            i = i + 1
            # 两肩中点
            if bs == 0:
                if i == 1:
                    point_one = detector.midpoint(img, 11, 12)
                elif i == 10:
                    point_ten = detector.midpoint(img, 11, 12)
                    point_foot = detector.midpoint(img, 29, 30)
                    spineV = int(math.hypot(point_ten['x'] - point_one['x'], point_ten['y'] - point_one['y']))
                    height_all = int(math.hypot(point_foot['x'] - point_one['x'], point_foot['y'] - point_one['y']))
                    ratio = spineV / height_all
                    if ratio > 0.25:
                        bs = 1
                    else:
                        i = 0

                    # print(length)
            # if bs==1:
            if True:
                # 两髋中心点
                point_kuan = detector.midpoint(img, 23, 24, draw=False)
                point_foot = detector.midpoint(img, 29, 30, draw=False)
                # 两脚中点

                baseH = (point_kuan['y'] - point_foot['y'])
                if baseH > -40 and i < 30:
                    bs = 2
                elif baseH < -40:
                    bs = 0
                    i = 0
            if bs == 2:
                cv2.putText(img, str("fall"), (450, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 0), 5)
        else:
            bs = 0
            i = 0
        print("%.3f" % ratio, "%.3f" % baseH, i, bs)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
    return img,i
