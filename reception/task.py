# -*- coding=utf-8 -*-
import os, django, json, datetime
from django.utils.timezone import now, timedelta

# date = now().date() + timedelta(days=-1) #昨天
# date = now().date() + timedelta(days=0) #今天
# date = now().date() + timedelta(days=1) #明天
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "education.settings")  # project_name 项目名称
django.setup()
from admin01.models import *
from admin01.serializer import *
import time

import redis
from django.core.mail import send_mail
from celery import task
from education import settings
from admin01.models import *
from utils.redis_pool import POOL


@task
def send(token, email):
    time.sleep(10)
    # 测试使用
    title = '实验楼在线教育平台注册激活信息'
    content = '<a href="http://127.0.0.1:8000/reg/?token=' + token + '">点击激活账号</a>'
    send_mail(title, content, settings.EMAIL_FORM, [email], html_message=content)
    return True


@task
def send1(token, email):
    time.sleep(10)
    # 测试使用
    title = '实验楼在线教育平台忘记密码验证信息'
    content = '<a href="http://127.0.0.1:8000/uploadpwd/?token=' + token + '">点击验证</a>'
    send_mail(title, content, settings.EMAIL_FORM, [email], html_message=content)
    return True


def write_into_redis():
    conn = redis.Redis(connection_pool=POOL)
    # 删掉已经过期的商品
    yesterdayList = Sk.objects.filter(act__date=now().date(-1) + timedelta(days=0))
    if yesterdayList:
        yesterdayList.delete()
        # 查询当天日期内的活动课程
    skList = Sk.objects.filter(act__date=now().date() + timedelta(days=0))

    # 将当天活动的课程放入redis
    if skList:
        skList = SkSerializersModel(skList, many=True)
        conn.hset('course', str(datetime.datetime.now())[:10], json.dumps(skList.data))
        conn.expire('course', 86440)  # 设置过期时间
