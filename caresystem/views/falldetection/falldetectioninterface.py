# 导入包

import numpy as np
import time
import cv2
import caresystem.views.falldetection.PoseModule as pm
import math
from caresystem.views.dataManage import addEvent

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
point_one = None
insert = 0
fall_timing = 0
fall_start_time = 0
fall_limit_time = 1
difference = 0


def falldetection(success, img):
    global count, dir, pTime, bs, ratio, height_all, baseH, point_one, insert, fall_timing, fall_start_time, fall_end_time
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

                baseH = (point_foot['y'] - point_hip['y'])
                mark = math.sqrt(
                    math.pow(point_shouder['x'] - point_hip['x'], 2) + math.pow(point_shouder['y'] - point_hip['y'], 2))
                print(baseH, mark)
                if baseH < mark:
                    bs = 2
                elif baseH > mark:
                    bs = 0
            if bs == 2:
                cv2.putText(img, str("fall"), (450, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 0), 5)
                if fall_timing == 0:
                    fall_timing = 1
                    fall_start_time = time.time()
                else:
                    fall_end_time = time.time()
                    difference = fall_end_time - fall_start_time
                if difference < fall_limit_time:
                    print("忽略")
                else:
                    if insert == 0:
                        # 插入数据库
                        print("跌倒")
                        addEvent('Unknown', '跌倒', '院子')
                        insert = 1
        else:
            bs = 0
            insert = 0
            fall_timing = 0
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
    return img
