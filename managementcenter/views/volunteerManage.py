# 义工信息管理
import datetime
import json

from django.core import serializers
from django.forms import model_to_dict
from django.utils import timezone
import pytz
from managementcenter.views import globeFunction
from managementcenter import models


def addVolunteerInfo(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    idcard = json_data["idcard"]
    print(idcard)
    if models.volunteer_info.objects.filter(idcard=idcard).exists():
        return {'msg': '工作人员信息已经存在，请查看信息是否填写有误，或者选择更新信息', "code": '205'}

    birthday = datetime.date(*map(int, json_data["birthday"].split('-')))
    now_time = globeFunction.get_now_time()
    print(birthday)
    try:
        volunteer = models.volunteer_info(volunteername=json_data["volunteername"],sex=json_data["sex"],
                                            phone=json_data["phone"], idcard=json_data["idcard"], birthday=birthday,
                                            checkindate=now_time, description=json_data["description"], created=now_time,
                                            createby=json_data["username"])
        volunteer.save()
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}

    try:
        face = models.face_recognition_info(identity="volunteer",identity_id=volunteer.ID,name=json_data["volunteername"])
        face.save()
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}
    return {'msg': '添加成功', "code": '200', "id": face.ID}

def updateVolunteerInfo(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    id = json_data["id"]
    try:
        models.volunteer_info.objects.filter(ID=id).update(phone=json_data["phone"], description=json_data["description"],
                                                           updated=globeFunction.get_now_time(), updateby=json_data["username"])
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}
    return {'msg': '更新成功', "code": '200'}

def checkoutVolunteer(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    id = json_data["id"]

    try:
        models.volunteer_info.objects.filter(ID=id).update(checkoutdate=globeFunction.get_now_time(),
                                                           description=json_data["description"],
                                                           updated=globeFunction.get_now_time(), updateby=json_data["username"])
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}
    return {'msg': '更新成功', "code": '200'}

def checkVolunteerById(request):
    id = request.GET["id"]
    print(id)
    if id:
        try:
            volunteer_list = models.volunteer_info.objects.get(ID=id)
        except:
            return {'msg': '不存在本信息，请检查id是否输入错误', "code": '204'}
        res = model_to_dict(volunteer_list)
        return {'msg': '获取成功', "code": '200', 'volunteerList': res}
    else:
        return {'msg': '请输入id', "code": '205'}

def getVolunteerList(request):
    try:
        volunteer_list = models.volunteer_info.objects.all()
    except:
        return {'msg': '不存在本信息', "code": '204'}
    res = []
    for i in volunteer_list:
        res.append(model_to_dict(i))
    return {'msg': '获取成功', "code": '200', 'volunteerList': res}

# 获取义工数量
def getVolunteerNum(request):
    try:
        volunteer_list = models.volunteer_info.objects.all()
    except:
        return {'msg': '不存在本信息', "code": '404'}
    volunteernum = len(volunteer_list)
    print(volunteernum)
    return {'msg':'获取成功','code': '200','oldnum': volunteernum}