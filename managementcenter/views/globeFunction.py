from django.utils import timezone
import pandas
import csv
import pytz
import json
import datetime

def get_now_time():
    """获取当前时间"""
    tz = pytz.timezone('Asia/Shanghai')
    # 返回时间格式的字符串
    now_time = timezone.now().astimezone(tz=tz)
    now_time_str = now_time.strftime("%Y.%m.%d %H:%M:%S")

    # 返回datetime格式的时间
    now_time = timezone.now().astimezone(tz=tz).strftime("%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')
    return now

def change_type(byte):
    if isinstance(byte,bytes):
        return str(byte,encoding="utf-8")
    return json.JSONEncoder.default(byte)

def write_info_to_csv(path, id, name, type):
    with open(path, 'a+', encoding='utf8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, name, type])

