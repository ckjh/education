import datetime
import json

import redis

from utils.redis_pool import POOL
import os, django
from django.utils.timezone import now, timedelta

# date = now().date() + timedelta(days=-1) #昨天
# date = now().date() + timedelta(days=0) #今天
# date = now().date() + timedelta(days=1) #明天
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "education.settings")  # project_name 项目名称
django.setup()
from admin01.models import *
from admin01.serializer import *


def write_into_redis():
    conn = redis.Redis(connection_pool=POOL)
    # 删掉已经过期的商品
    # yesterdayList = Sk.objects.filter(act__date=now().date(-1) + timedelta(days=0))
    # if yesterdayList:
    #     yesterdayList.delete()
        # 查询当天日期内的活动课程
    skList = Sk.objects.filter(act__date=now().date() + timedelta(days=0))

    # 将当天活动的课程放入redis
    if skList:
        skList = SkSerializersModel(skList, many=True)
        conn.hset('course', str(datetime.datetime.now())[:10], json.dumps(skList.data))
        conn.expire('course', 86440)  # 设置过期时间


write_into_redis()
# print(now().date() + timedelta(days=0))
