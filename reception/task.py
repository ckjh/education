# -*- coding=utf-8 -*-
import time
from django.core.mail import send_mail
from celery import task
from education import settings
@task
def send(email):
    time.sleep(10)
    # 测试使用
    token = 'ok'
    title = '村口集合'
    content = '<a href="http://127.0.0.1:8000/user/active/?token=' + token + '">激活账号</a>'
    send_mail(title, content, settings.EMAIL_FORM, [email], html_message=content)
    return True