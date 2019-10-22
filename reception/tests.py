import datetime, json, redis, os, django
from utils.redis_pool import POOL
from django.utils.timezone import now, timedelta

# date = now().date() + timedelta(days=-1) #昨天
# date = now().date() + timedelta(days=0) #今天
# date = now().date() + timedelta(days=1) #明天
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "education.settings")  # project_name 项目名称
django.setup()
from admin01.serializer import *


def write_into_redis():
    conn = redis.Redis(connection_pool=POOL)
    # 删掉已经过期的商品(昨天的)
    yesterdayList = Sk.objects.filter(act__date=datetime.datetime.now() + timedelta(days=-1))
    if yesterdayList:
        pass
        # yesterdayList.delete()
        # 查询当天日期内的活动课程
    skList = Sk.objects.filter(act__date=datetime.datetime.now())

    # 将当天活动的课程放入redis
    if skList:
        for one in skList:
            one_course = SkSerializersModel(one, many=False)
            print(one_course)
            conn.hset('course' + str(datetime.datetime.now())[:10],
                      (str(one.act_id) + ',' + str(one.time_id) + ',' + str(one.course_id)),
                      json.dumps(one_course.data))
        conn.expire('course' + str(datetime.datetime.now())[:10], 87000)  # 设置过期时间
    else:
        print('今天没活动')


"""
执行任务
"""




if __name__ == '__main__':
    write_into_redis()

