from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from caresystem.views import mobile,dataManage

def test01(request):
    result = dataManage.addEvent(2,"互动","与护工哈哈进行互动")
    return JsonResponse('test02', safe=False)

# 获取事件列表
def getEventInfo(request):
    result = dataManage.getEventInfo(request)
    return JsonResponse(result, safe=False)