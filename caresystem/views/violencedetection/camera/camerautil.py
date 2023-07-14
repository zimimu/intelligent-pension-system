# -*- coding: utf-8 -*-

import cv2
import threading

from ultralytics import YOLO

i = 0

# model = YOLO('E:/xxq/demo04/caresystem/views/models/best-violence.pt')
model = YOLO('F:/SummerVacation2023/intelligent-pension-system/caresystem/views/models/best-violence.pt')

class RecordingThread(threading.Thread):
    def __init__(self, name, camera, save_video_path):
        threading.Thread.__init__(self)
        self.name = name
        self.isRunning = True

        self.cap = camera
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # MJPG
        self.out = cv2.VideoWriter(save_video_path, fourcc, 20.0,
                                   (640, 480), True)

    def run(self):
        while self.isRunning:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.flip(frame, 1)
                self.out.write(frame)

        self.out.release()

    def stop(self):
        self.isRunning = False

    def __del__(self):
        self.out.release()


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

    def get_frame(self):
        global i
        ret, frame = self.cap.read()

        if ret:
            frame = cv2.flip(frame, 1)
            # frame=checkingstrangersandfacialexpression(ret, frame)
            # frame,i=falldetection(ret, frame,i)
            # frame=volunteeractivity(ret,frame)
            # frame=fire_detection(frame)
            # frame=checkingfence(frame)
            # frame,i=collectingfaces(frame,108,i)
            frame = model(frame)
            frame = frame[0].plot()
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()

        else:
            return None

    def start_record(self, save_video_path):
        self.is_record = True
        self.recordingThread = RecordingThread(
            "Video Recording Thread",
            self.cap, save_video_path)
        self.recordingThread.start()

    def stop_record(self):
        self.is_record = False

        if self.recordingThread is not None:
            self.recordingThread.stop()
