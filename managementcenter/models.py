from django.db import models

# Create your models here.
# 老人信息
class oldperson_info(models.Model):
    ID = models.AutoField(primary_key=True)
    oldname = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)
    idcard = models.CharField(max_length=50)
    birthday = models.DateTimeField()
    checkindate = models.DateTimeField()
    checkoutdate = models.DateTimeField(null=True)
    roomnum = models.CharField(max_length=50)
    firstguardianname = models.CharField(max_length=50)
    firstguardianrela = models.CharField(max_length=50)
    firstguardianphone = models.CharField(max_length=50)
    firstguardianwechat = models.CharField(max_length=50)
    secondguardianname = models.CharField(max_length=50)
    secondguardianrela = models.CharField(max_length=50)
    secondguardianphone = models.CharField(max_length=50)
    secondguardianwechat = models.CharField(max_length=50)
    healthstate = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created = models.DateTimeField()
    createby = models.CharField(max_length=50)
    updated = models.DateTimeField(null=True)
    updateby = models.CharField(max_length=50, null=True)


class employee_info(models.Model):
    ID = models.AutoField(primary_key=True)
    employeename = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=50, null=True)
    idcard = models.CharField(max_length=50, null=True)
    birthday = models.DateTimeField(null=True)
    hiredate = models.DateTimeField(null=True)
    resigndate = models.DateTimeField(null=True)
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(null=True)
    createby = models.CharField(max_length=50, null=True)
    updated = models.DateTimeField(null=True)
    updateby = models.CharField(max_length=50, null=True)


class volunteer_info(models.Model):
    ID = models.AutoField(primary_key=True)
    volunteername = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)
    idcard = models.CharField(max_length=50)
    birthday = models.DateTimeField()
    checkindate = models.DateTimeField()
    checkoutdate = models.DateTimeField(null=True)
    description = models.CharField(max_length=200)
    created = models.DateTimeField()
    createby = models.CharField(max_length=50)
    updated = models.DateTimeField(null=True)
    updateby = models.CharField(max_length=50, null=True)


class face_recognition_info(models.Model):
    ID = models.AutoField(primary_key=True)
    identity = models.CharField(max_length=50)
    identity_id = models.IntegerField()
    name = models.CharField(max_length=50)


