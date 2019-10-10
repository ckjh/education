# -*- coding=utf-8 -*-
import time
from django.core.mail import send_mail
from celery import task
from education import settings
@task
def send(token,email):
    time.sleep(10)
    # 测试使用
    title = '实验楼在线教育平台注册激活信息'
    content = '<a href="http://127.0.0.1:8000/reg/?token=' + token + '">点击激活账号</a>'
    send_mail(title, content, settings.EMAIL_FORM, [email], html_message=content)
    return True


@task
def send1(token,email):
    time.sleep(10)
    # 测试使用
    title = '实验楼在线教育平台忘记密码验证信息'
    content = '<a href="http://127.0.0.1:8000/uploadpwd/?token=' + token + '">点击验证</a>'
    send_mail(title, content, settings.EMAIL_FORM, [email], html_message=content)
    return True