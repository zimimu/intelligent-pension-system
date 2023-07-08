# 工作人员信息管理
import datetime
import json

from django.core import serializers
from django.forms import model_to_dict
from django.utils import timezone
import pytz
from managementcenter.views import globeFunction
from managementcenter import models


def addEmployInfo(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    idcard = json_data["idcard"]
    print(idcard)
    if models.employee_info.objects.filter(idcard=idcard).exists():
        return {'msg': '工作人员信息已经存在，请查看信息是否填写有误，或者选择更新信息', "code": '205'}

    birthday = datetime.date(*map(int, json_data["birthday"].split('-')))
    now_time = globeFunction.get_now_time()
    print(birthday)
    try:
        employee = models.employee_info(employeename=json_data["employeename"],sex=json_data["sex"],
                                            phone=json_data["phone"], idcard=json_data["idcard"], birthday=birthday,
                                            hiredate=now_time, description=json_data["description"], created=now_time,
                                            createby=json_data["username"])
        employee.save()
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}

    try:
        face = models.face_recognition_info(identity="employee",identity_id=employee.ID,name=json_data["employeename"])
        face.save()
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}

    return {'msg': '添加成功', "code": '200',"id": face.ID}

def updateEmployInfo(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    id = json_data["id"]
    try:
        models.employee_info.objects.filter(ID=id).update(phone=json_data["phone"], description=json_data["description"],
                                                           updated=globeFunction.get_now_time(), updateby=json_data["username"])
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}
    return {'msg': '更新成功', "code": '200'}

def resignEmployee(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    id = json_data["id"]

    try:
        models.employee_info.objects.filter(ID=id).update(resigndate=globeFunction.get_now_time(),
                                                           description=json_data["description"],
                                                           updated=globeFunction.get_now_time(), updateby=json_data["username"])
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}
    return {'msg': '更新成功', "code": '200'}

def checkEmployeeById(request):
    id = request.GET["id"]
    print(id)
    if id:
        try:
            employee_list = models.employee_info.objects.get(ID=id)
        except:
            return {'msg': '不存在本信息，请检查id是否输入错误', "code": '204'}
        res = model_to_dict(employee_list)
        return {'msg': '获取成功', "code": '200', 'employeeList': res}
    else:
        return {'msg': '请输入id', "code": '205'}

def getEmployeeList(request):
    try:
        employee_list = models.employee_info.objects.all()
    except:
        return {'msg': '不存在本信息', "code": '204'}
    res = []
    for i in employee_list:
        res.append(model_to_dict(i))
    return {'msg': '获取成功', "code": '200', 'employeeList': res}