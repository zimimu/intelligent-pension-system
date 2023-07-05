from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from caresystem import models

def test01(request):
    return JsonResponse('test02', safe=False)

def orm(request):
    # 测试ORM操作表中的数据
    data_list = models.test.objects.all()
    for obj in data_list:
        print(obj.id, obj.name, obj.password, obj.age)
    return JsonResponse('orm', safe=False)