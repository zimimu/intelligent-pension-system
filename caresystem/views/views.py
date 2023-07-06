from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from caresystem import models
from caresystem.views import VideoCamera


def test01(request):
    return JsonResponse('test02', safe=False)

def orm(request):
    # 测试ORM操作表中的数据
    data_list = models.test.objects.all()
    for obj in data_list:
        print(obj.id, obj.name, obj.password, obj.age)
    return JsonResponse('orm', safe=False)

# 获取视频流
def camera(request):
    return JsonResponse(video_stream(),mimetype='multipart/x-mixed-replace; boundary=frame')

# 视频流方法
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

