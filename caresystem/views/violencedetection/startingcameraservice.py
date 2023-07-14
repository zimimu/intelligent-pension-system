# -*- coding: utf-8 -*-

"""
启动摄像头主程序

用法:
python startingcameraservice.py
python startingcameraservice.py --location room

直接执行即可启动摄像头，浏览器访问即可看到
摄像头实时画面

"""

from caresystem.views.violencedetection.camera import VideoCamera

video_camera = None
global_frame = None


def video_stream():
    global video_camera
    global global_frame

    if video_camera is None:
        video_camera = VideoCamera()

    while True:
        frame = video_camera.get_frame()
        if frame is not None:
            global_frame = frame
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame
                   + b'\r\n\r\n')
        else:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n'
                   + global_frame + b'\r\n\r\n')
