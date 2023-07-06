import json

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from usercenter import models

def test01(request):
    return JsonResponse('test01', safe=False)

def userLogin(request):
    print("登陆请求被触发")
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)
    username = json_data["username"]
    password = json_data["password"]

    if username and password:
        try:
            user_list = models.user.objects.get(username=username)
        except:
            return JsonResponse({'msg': '未进行注册', "code": '401'}, safe=False)
        if user_list.password == password:
            return JsonResponse({'msg': '密码正确', "code": '200'}, safe=False)
        else:
            return JsonResponse({'msg': '密码错误', "code": '401'}, safe=False)
    else:
        return JsonResponse({'msg': '未输入账号或密码', "code": '401'}, safe=False)

def changePw(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    username = json_data["username"]
    password = json_data["password"]
    try:
        models.user.objects.filter(username=username).update(password=password)
    except:
        return JsonResponse({'msg': '服务器错误，请重试', "code": '500'}, safe=False)
    return JsonResponse({'msg': '修改成功', "code": '200'}, safe=False)

def changeUserInfo(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    username = json_data["username"]
    description = json_data["description"]
    email = json_data["email"]
    phone = json_data["phone"]
    try:
        models.user.objects.filter(username=username).update(email=email,description=description,phone=phone)
    except:
        return JsonResponse({'msg': '服务器错误，请重试', "code": '500'}, safe=False)
    return JsonResponse({'msg': '修改成功', "code": '200'}, safe=False)

def addNewUser(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    username = json_data["username"]
    password = json_data["password"]
    realname = json_data["realname"]
    email = json_data["email"]
    sex = json_data["sex"]
    phone = json_data["phone"]
    description = json_data["description"]
    try:
        models.user.objects.create(username=username, password=password, realname=realname, email=email,
                                   sex=sex, phone=phone, description=description)
    except:
        return JsonResponse({'msg': '服务器错误，请重试', "code": '500'}, safe=False)
    return JsonResponse({'msg': '添加成功', "code": '200'}, safe=False)

# 获取用户信息
def getuser(request):
    print("获取用户信息开始执行")
    username = request.GET.get("username")
    print(username)
    try:
        user_list = models.user.objects.get(username=username)
    except:
        return JsonResponse({'msg': '不存在该用户', "code": '401', 'status_code': '2'}, safe=False)

    return JsonResponse({'msg': '获取成功', 'code': '200', 'status_code': '1',
                         'username': username, 'password': user_list.password,
                         'realname': user_list.realname, 'email': user_list.email,
                         'sex': user_list.sex, 'phone': user_list.phone,
                         'description': user_list.description}, safe=False)

# 测试返回列表使用
# def getuser(request):
#     username = request.GET.get("username")
#     print(username)
#     try:
#         user = models.user.objects.get(username=username)
#     except:
#         return JsonResponse({'msg': '不存在该用户', "code": '401', 'status_code': '2'}, safe=False)
#     print(type(user))
#     res = model_to_dict(user)
#     # 序列化
#     # json_data = json.dumps(list(user), cls=DjangoJSONEncoder)
#     # user_list = serializers.serialize('json', user, ensure_ascii=False)
#     # user_list = json.loads(user_list)
#     return JsonResponse({'msg': '获取成功', 'code': '200', 'status_code': '1', 'user_list': res},safe=False)