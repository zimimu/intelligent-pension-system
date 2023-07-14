# -*- coding: utf-8 -*-

import cv2
import threading

from managementcenter.views.faceCollection.collectingfacesinterface import collectingfaces
from managementcenter.views.faceCollection.facial import FaceUtil

i = 0


class VideoCamera(object):
    def __init__(self):
        # Open a camera
        self.cap = cv2.VideoCapture(0)

        # Initialize video recording environment
        self.is_record = False
        self.out = None

        # Thread for recording
        self.recordingThread = None

    def __del__(self):
        self.cap.release()

    def get_frame(self, id):
        print("get_frame函数被调用，获取的id是：")
        print(id)
        global i
        ret, frame = self.cap.read()

        if ret:
            frame = cv2.flip(frame, 1)
            frame, i = collectingfaces(frame, id, i)
            ret, jpeg = cv2.imencode('.jpg', frame)
            if i == 119:
                self.cap.release()
            return jpeg.tobytes()

        else:
            return None
