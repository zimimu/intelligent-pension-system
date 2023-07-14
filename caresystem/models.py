from django.db import models

# Create your models here.

# 事件表
class event_info(models.Model):
    ID = models.AutoField(primary_key=True)
    event_type = models.CharField(max_length=50)
    event_date = models.DateTimeField()
    event_desc = models.CharField(max_length=200)
    event_place = models.CharField(max_length=50, null=True)
    oldperson_id = models.IntegerField(null=True)
    status = models.IntegerField()
