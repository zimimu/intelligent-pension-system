from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def test03(request):
    return JsonResponse('test03', safe=False)