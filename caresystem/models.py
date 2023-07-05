from django.db import models

# Create your models here.

# 创表
class test(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

test.objects.create(name="yyz", password="123", age=21)