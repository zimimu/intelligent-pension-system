from django.db import models

# Create your models here.
class user(models.Model):
    ID = models.AutoField(primary_key=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    realname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

