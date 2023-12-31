import json

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from usercenter import models


def userLogin(request):
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
            return JsonResponse({'msg': '未进行注册', "code": '204', "status_code": "1"}, safe=False)
        if user_list.password == password:
            return JsonResponse({'msg': '密码正确', "code": '200', "status_code": "2"}, safe=False)
        else:
            return JsonResponse({'msg': '密码错误', "code": '204', "status_code": "3"}, safe=False)
    else:
        return JsonResponse({'msg': '未输入账号或密码', "code": '204', "status_code": "4"}, safe=False)

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

# 获取个人中心信息
def getuser(request):
    username = request.GET["username"]
    print("getuser函数调用")
    print(username)

    if username:
        try:
            user = models.user.objects.get(username=username)
            print(user)
        except:
            return JsonResponse({'msg': '不存在本信息', "code": '401'},safe=False)

        return JsonResponse({'msg': '获取成功', "code": '200', 'username': user.username,
                'password': user.password, 'realname': user.realname,
                'email': user.email, 'sex': user.sex, 'phone': user.phone,
                'description': user.description},safe=False)
    else:
        return JsonResponse({'msg': '请输入id', "code": '205'},safe=False)

# 获取管理员数量
def getUserNum(request):
    try:
        user_list = models.user.objects.all()
    except:
        return JsonResponse({'msg': '记录不存在', 'code': '404'}, safe=False)
    usernum = len(user_list)
    return JsonResponse({'msg': '获取成功', 'code':'200', 'usernum': usernum}, safe=False)



