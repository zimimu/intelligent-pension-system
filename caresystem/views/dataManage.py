import datetime
import json

from django.core import serializers
from django.forms import model_to_dict
from django.utils import timezone
import pytz
from managementcenter.views import globeFunction
from caresystem import models
from django.core.cache import cache
from django.shortcuts import render, HttpResponse
import time
from django.views.decorators.cache import cache_page

def get_now_time():
    """获取当前时间"""
    tz = pytz.timezone('Asia/Shanghai')
    # 返回时间格式的字符串
    now_time = timezone.now().astimezone(tz=tz)
    now_time_str = now_time.strftime("%Y.%m.%d %H:%M:%S")
    # 返回datetime格式的时间
    now_time = timezone.now().astimezone(tz=tz).strftime("%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')
    return now

def addEvent(oldPersonId, event_type, event_desc):
    now = get_now_time()
    try:
        event = models.event_info(oldperson_id=oldPersonId, event_desc=event_desc,
                                  event_type=event_type,event_date=now)
        event.save()
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}

    return {'msg': '添加成功', "code": '200'}


def getEmotionEvent(request):
    emotionList = cache.get('emotion_list')
    if not emotionList:
        try:
            emotionList = models.event_info.objects.filter(event_type="情绪")
            cache.set('emotion_list', emotionList, 10)
        except:
            return {'msg': '不存在本信息', "code": '204'}
    res = []
    for i in emotionList:
        res.append(model_to_dict(i))
    return {'msg': '获取成功', "code": '200', 'emotion_list': res}

def getInteractEvent(request):
    interactList = cache.get('interact_list')
    if not interactList:
        try:
            interactList = models.event_info.objects.filter(event_type="互动")
            cache.set('interact_list', interactList, 10)
        except:
            return {'msg': '不存在本信息', "code": '204'}
    res = []
    for i in interactList:
        res.append(model_to_dict(i))
    return {'msg': '获取成功', "code": '200', 'interact_list': res}

def getFallEvent(request):
    fallList = cache.get('fall_list')
    if not fallList:
        try:
            fallList = models.event_info.objects.filter(event_type="互动")
            cache.set('fall_list', fallList, 10)
        except:
            return {'msg': '不存在本信息', "code": '204'}
    res = []
    for i in fallList:
        res.append(model_to_dict(i))
    return {'msg': '获取成功', "code": '200', 'fall_list': res}


def getIntrusionEvent(request):
    intrusionList = cache.get('intrusion_list')
    if not intrusionList:
        try:
            intrusionList = models.event_info.objects.filter(event_type="互动")
            cache.set('intrusion_list', intrusionList, 10)
        except:
            return {'msg': '不存在本信息', "code": '204'}
    res = []
    for i in intrusionList:
        res.append(model_to_dict(i))
    return {'msg': '获取成功', "code": '200', 'intrusion_list': res}

def getEventInfo(request):
    try:
        event_list = models.event_info.objects.all()
    except:
        return {'msg': '不存在本信息', "code": '204'}
    res = []
    for i in event_list:
        res.append(model_to_dict(i))
    return {'msg': '获取成功', "code": '200', 'oldList': res}