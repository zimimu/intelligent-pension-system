# # -*- coding: utf-8 -*-
#
# '''
# 启动摄像头主程序
#
# 用法:
# python startingcameraservice.py
# python startingcameraservice.py --location room
#
# 直接执行即可启动摄像头，浏览器访问 http://192.168.1.156:5001/ 即可看到
# 摄像头实时画面
#
# '''
import argparse
# # from flask import Flask, render_template, Response, request
# # from oldcare.camera import VideoCamera
# from caresystem.views import VideoCamera
#
# 传入参数
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--location", required=False,
                default = 'room', help="")
args = vars(ap.parse_args())
# location = args['location']
#
# if location not in ['room', 'yard', 'corridor', 'desk']:
#     raise ValueError('location must be one of room, yard, corridor or desk')
#
# # API
#
video_camera = None
global_frame = None

# @app.route('/')
# def index():
#     return render_template(location + '_camera.html')

# @app.route('/record_status', methods=['POST'])
# def record_status():
#     global video_camera
#     if video_camera == None:
#         video_camera = VideoCamera()
#
#     status = request.form.get('status')
#     print(status)
#     save_video_path = request.form.get('save_video_path')
#     if status == "true":
#         video_camera.start_record(save_video_path)
#         return 'start record'
#     else:
#         video_camera.stop_record()
#         return 'stop record'


# def video_stream():
#     global video_camera
#     global global_frame
#
#     if video_camera is None:
#         video_camera = VideoCamera()
#
#     while True:
#         frame = video_camera.get_frame()
#
#         if frame is not None:
#             global_frame = frame
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame
#                    + b'\r\n\r\n')
#         else:
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n'
#                    + global_frame + b'\r\n\r\n')
#

# @app.route('/video_viewer')
# def video_viewer():
#     return Response(video_stream(),mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', threaded=True, port=5001)

