from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

def test01(request):
    return JsonResponse('test01', safe=False)