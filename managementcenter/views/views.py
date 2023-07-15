from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, StreamingHttpResponse
from multiprocessing import Pool
from managementcenter.views import globeFunction
from managementcenter.views import oldManage,employeeManage,volunteerManage
from managementcenter.views.faceCollection import startingcameraservice


# 增加老人信息
def addOldInfo(request):
    result = oldManage.addOldInfo(request)
    return JsonResponse(result, safe=False)

# 更新老人信息
def updateOldInfo(request):
    result = oldManage.updateOldInfo(request)
    return JsonResponse(result, safe=False)

# 老人出院办理
def checkoutOld(request):
    result = oldManage.checkoutOld(request)
    return JsonResponse(result, safe=False)

# 根据id查询老人信息
def checkOldById(request):
    result = oldManage.checkOldById(request)
    return JsonResponse(result, safe=False)

# 获取所有老人信息
def getOldList(request):
    result = oldManage.getOldList(request)
    return JsonResponse(result, safe=False)

# 获取老人数量
def getOldNum(request):
    result = oldManage.getOldNum(request)
    return JsonResponse(result,safe=False)

# 老人年龄分布直方图
def getOldAgeNum(request):
    result = oldManage.getOldAgeNum(request)
    return JsonResponse(result,safe=False)

# 添加工作人员信息
def addEmployeeInfo(request):
    result = employeeManage.addEmployInfo(request)
    return JsonResponse(result, safe=False)

#更新工作人员信息
def updateEmployeeInfo(request):
    result = employeeManage.updateEmployInfo(request)
    return JsonResponse(result, safe=False)

# 办理工作人员离职
def resignTmployee(request):
    result = employeeManage.resignEmployee(request)
    return JsonResponse(result, safe=False)

# 按id查找工作人员
def checkEmployeeById(request):
    result = employeeManage.checkEmployeeById(request)
    return JsonResponse(result, safe=False)

# 获取工作人员列表
def getEmployeeList(request):
    result = employeeManage.getEmployeeList(request)
    return JsonResponse(result, safe=False)

# 获取工作人员数量
def getEmployeeNum(request):
    result = employeeManage.getEmployeeNum(request)
    return JsonResponse(result, safe=False)

# 新增义工
def addVolunteerInfo(request):
    result = volunteerManage.addVolunteerInfo(request)
    return JsonResponse(result, safe=False)

# 更新义工信息
def updateVolunteerInfo(request):
    result = volunteerManage.updateVolunteerInfo(request)
    return JsonResponse(result, safe=False)

# 进行义工签出操作
def checkoutVolunteer(request):
    result = volunteerManage.checkoutVolunteer(request)
    return JsonResponse(result, safe=False)

# 按id查找义工信息
def checkVolunteerById(request):
    result = volunteerManage.checkVolunteerById(request)
    return JsonResponse(result, safe=False)

# 获取义工列表
def getVolunteerList(request):
    result = volunteerManage.getVolunteerList(request)
    return JsonResponse(result, safe=False)

# 获取老人监护人电话号
def getGuartionPhone(request):
    result = oldManage.get_guardian_phone(request)
    return JsonResponse(result, safe=False)

def getFaceCollectionStream(request):
    id = request.GET["id"]
    print("getFaceCollectionStream函数被调用，获取的id是：")
    print(id)
    return StreamingHttpResponse(startingcameraservice.video_stream(id), content_type='multipart/x-mixed-replace; boundary=frame')

# 获取义工数量
def getVolunteerNum(request):
    result = volunteerManage.getVolunteerNum(request)
    return JsonResponse(result, safe=False)

