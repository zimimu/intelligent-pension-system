# 老人信息管理
import datetime
import json

from managementcenter.views import globeFunction
from dateutil.relativedelta import relativedelta
from django.forms import model_to_dict
from django.utils import timezone
import pytz

from managementcenter import models


def get_now_time():
    """获取当前时间"""
    tz = pytz.timezone('Asia/Shanghai')
    # 返回时间格式的字符串
    now_time = timezone.now().astimezone(tz=tz)
    now_time_str = now_time.strftime("%Y.%m.%d %H:%M:%S")

    # 返回datetime格式的时间
    now_time = timezone.now().astimezone(tz=tz).strftime("%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')
    print(now)
    return now


def addOldInfo(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    idcard = json_data["idcard"]

    if models.oldperson_info.objects.filter(idcard=idcard).exists():
        return {'msg': '老人信息已经存在，请查看信息是否填写有误，或者选择更新信息', "code": '205'}

    birthday = datetime.date(*map(int, json_data["birthday"].split('-')))
    print(birthday)
    now_time = get_now_time()

    try:
        old = models.oldperson_info(oldname=json_data["oldname"], sex=json_data["sex"], phone=json_data["phone"],
                                    idcard=idcard, birthday=birthday, checkindate=now_time,
                                    roomnum=json_data["roomnum"], firstguardianname=json_data["firstguardianname"],
                                    firstguardianrela=json_data["firstguardianrela"],
                                    firstguardianphone=json_data["firstguardianphone"],
                                    firstguardianwechat=json_data["firstguardianwechat"],
                                    secondguardianname=json_data["secondguardianname"],
                                    secondguardianrela=json_data["secondguardianrela"],
                                    secondguardianphone=json_data["secondguardianphone"],
                                    secondguardianwechat=json_data["secondguardianwechat"],
                                    healthstate=json_data["healthstate"], description=json_data["description"],
                                    created=now_time, createby=json_data["username"])
        old.save()
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}

    try:
        face = models.face_recognition_info(identity="old_people", identity_id=old.ID, name=json_data["oldname"])
        face.save()
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}
    globeFunction.write_info_to_csv("", face.ID, json_data["oldname"], "old_people")
    return {'msg': '添加成功', "code": '200', "id": face.ID}


def updateOldInfo(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    id = json_data["id"]
    try:
        models.oldperson_info.objects.filter(ID=id).update(phone=json_data["phone"], roomnum=json_data["roomnum"],
                                                           firstguardianname=json_data["firstguardianname"],
                                                           firstguardianrela=json_data["firstguardianrela"],
                                                           firstguardianphone=json_data["firstguardianphone"],
                                                           firstguardianwechat=json_data["firstguardianwechat"],
                                                           secondguardianname=json_data["secondguardianname"],
                                                           secondguardianrela=json_data["secondguardianrela"],
                                                           secondguardianphone=json_data["secondguardianphone"],
                                                           secondguardianwechat=json_data["secondguardianwechat"],
                                                           healthstate=json_data["healthstate"],
                                                           description=json_data["description"], updated=get_now_time(),
                                                           updateby=json_data["username"])
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}

    return {'msg': '更新成功', "code": '200'}


def checkoutOld(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    id = json_data["id"]

    try:
        models.oldperson_info.objects.filter(ID=id).update(checkoutdate=get_now_time(),
                                                           description=json_data["description"],
                                                           updated=get_now_time(), updateby=json_data["username"])
    except:
        return {'msg': '服务器错误，请重试', "code": '500'}

    return {'msg': '更新成功', "code": '200'}


def checkOldById(request):
    id = request.GET["id"]
    print(id)
    if id:
        try:
            old_list = models.oldperson_info.objects.get(ID=id)
            print(old_list)
        except:
            return {'msg': '不存在本信息，请检查id是否输入错误', "code": '204'}
        res = model_to_dict(old_list)
        return {'msg': '获取成功', "code": '200', 'oldList': res}
    else:
        return {'msg': '请输入id', "code": '205'}


def getOldList(request):
    try:
        old_list = models.oldperson_info.objects.all()
    except:
        return {'msg': '不存在本信息', "code": '204'}
    res = []
    for i in old_list:
        res.append(model_to_dict(i))
    return {'msg': '获取成功', "code": '200', 'oldList': res}


def get_guardian_phone(request):
    id = request.GET["id"]
    try:
        old_list = models.oldperson_info.objects.get(ID=id)
    except:
        return {'msg': '不存在本信息，请检查id是否输入错误', "code": '204'}
    res = model_to_dict(old_list)
    phone = res.get("firstguardianphone")
    return {'msg': '获取成功', "code": '200', 'phone': phone}

# 获取老人数量
def getOldNum(request):
    try:
        old_list = models.oldperson_info.objects.all()
    except:
        return {'msg': '不存在本信息', "code": '404'}
    oldnum = len(old_list)
    print(oldnum)
    return {'msg':'获取成功','code': '200','oldnum': oldnum}

# 老人年龄分布直方图
def getOldAgeNum(request):
    # 取出old 里面的生日日期
    try:
        old = list(models.oldperson_info.objects.values_list('birthday', flat=True))
    except:
        return {'msg': '不存在本信息', "code": '404'}
    # 计算old 的年龄，归类到数组age中
    today = datetime.datetime.today()
    temp = []
    age = []
    for i in range(0, len(old)):
        birthday = old[i]
        # print(birthday)
        temp.append(relativedelta(today, birthday))
        age.append(temp[i].years)
        # print("age:")
        # print(i)
        # print(age[i])
    array = [0, 0, 0, 0]
    for i in range(0, len(age)):
        if age[i] <= 50:
            array[0] = array[0] + 1
        elif 50 < age[i] <= 70:
            array[1] = array[1] + 1
        elif 70 < age[i] <= 90:
            array[2] = array[2] + 1
        else:
            array[3] = array[3] + 1
    print("array:")
    print(array)
    # 返回数组[],分别表示 0-50，50-70，70-90，90- 年龄段老人数目
    # array = [1, 20, 32, 6]

    return {'msg': '获取成功', 'code': 200, 'array': array}
