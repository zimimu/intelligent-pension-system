from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, StreamingHttpResponse

import caresystem
from caresystem.views import mobile,dataManage
from caresystem.views.facialexpression import startingcameraservice
from caresystem.views.falldetection import startingcameraservice
from caresystem.views.fencein import startingcameraservice
from caresystem.views.volunteeract import startingcameraservice
from caresystem.views.voiceChat import chatgpt

def test01(request):
    result = dataManage.addEvent(2,"互动","与护工哈哈进行互动")
    return JsonResponse('test02', safe=False)

# 获取事件列表
def getEventInfo(request):
    result = dataManage.getEventInfo(request)
    return JsonResponse(result, safe=False)

def getFacialExpressionStream(request):
    return StreamingHttpResponse(caresystem.views.facialexpression.startingcameraservice.video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')

def getFalldetectionStream(request):
    return StreamingHttpResponse(caresystem.views.falldetection.startingcameraservice.video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')

def getFenceinStream(request):
    return StreamingHttpResponse(caresystem.views.fencein.startingcameraservice.video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')

def getVolunteeractStream(request):
    return StreamingHttpResponse(caresystem.views.volunteeract.startingcameraservice.video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')

def getEmotionList(request):
    result = dataManage.getEmotionEvent(request)
    return JsonResponse(result, safe=False)

def getFallList(request):
    result = dataManage.getFallEvent(request)
    return JsonResponse(result, safe=False)

def getIntrusionList(request):
    result = dataManage.getIntrusionEvent(request)
    return JsonResponse(result, safe=False)

def getInteractList(request):
    result = dataManage.getInteractEvent(request)
    return JsonResponse(result, safe=False)

def changeEventStatus(request):
    result = dataManage.changeEventStatus(request)
    return JsonResponse(result, safe=False)

def getChatResult(request):
    result = chatgpt.ChatGPT(request)
    return JsonResponse(result, safe=False)

def addCallEvent(request):
    result = dataManage.addNewCall(request)
    return JsonResponse(result, safe=False)