# import datetime, json, redis, os, django
# from utils.redis_pool import POOL
# from django.utils.timezone import now, timedelta
#
# # date = now().date() + timedelta(days=-1) #昨天
# # date = now().date() + timedelta(days=0) #今天
# # date = now().date() + timedelta(days=1) #明天
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "education.settings")  # project_name 项目名称
# django.setup()
# from admin01.serializer import *
#
#
# def write_into_redis():
#     conn = redis.Redis(connection_pool=POOL)
#     # 删掉已经过期的商品(昨天的)
#     yesterdayList = Sk.objects.filter(act__date=now().date() + timedelta(days=-1))
#     if yesterdayList:
#         yesterdayList.delete()
#         # 查询当天日期内的活动课程
#     skList = Sk.objects.filter(act__date=now().date() + timedelta(days=0))
#
#     # 将当天活动的课程放入redis
#     if skList:
#         skList = SkSerializersModel(skList, many=True)
#         conn.hset('course', str(datetime.datetime.now())[:10], json.dumps(skList.data))
#         conn.expire('course', 87000)  # 设置过期时间
#
#
# write_into_redis()

"""
执行任务
"""
# -*- coding=utf-8 -*-
import math
from operator import *

# 例子中的数据相当于是一个用户字典{A:(a,b,d),B:(a,c),C:(b,e),D:(c,d,e)}
# 我们这样存储原始输入数据

dic = {'A': ('a', 'b', 'd', 'f', 'k'), 'B': ('a', 'c', 'f'), 'C': ('b', 'e', 'k'),
       'D': ('c', 'd', 'e', 'k'), 'E': {'c', 'k'}}  # 简单粗暴，记得加''


# 计算用户兴趣相似度
def Usersim(dicc):
    # 把用户-商品字典转成商品-用户字典（如图中箭头指示那样）
    item_user = dict()
    for u, items in dicc.items():
        for i in items:  # 文中的例子是不带评分的，所以用的是元组而不是嵌套字典。
            if i not in item_user.keys():
                item_user[i] = set()  # i键所对应的值是一个集合（不重复）。
            item_user[i].add(u)  # 向集合中添加用户。

    C = dict()  # 感觉用数组更好一些，真实数据集是数字编号，但这里是字符，这边还用字典。
    N = dict()
    for item, users in item_user.items():
        for u in users:
            if u not in N.keys():
                N[u] = 0  # 书中没有这一步，但是字典没有初始值不可以直接相加吧
            N[u] += 1  # 每个商品下用户出现一次就加一次，就是计算每个用户一共购买的商品个数。
            # 但是这个值也可以从最开始的用户表中获得。
            # 比如： for u in dic.keys():
            #             N[u]=len(dic[u])
            for v in users:
                if u == v:
                    continue
                if (u, v) not in C.keys():  # 同上，没有初始值不能+=
                    C[u, v] = 0
                C[u, v] += 1  # 这里我不清楚书中是不是用的嵌套字典，感觉有点迷糊。所以我这样用的字典。
    # 到这里倒排阵就建立好了，下面是计算相似度。
    W = dict()
    for co_user, cuv in C.items():
        W[co_user] = cuv / math.sqrt(N[co_user[0]] * N[co_user[1]])  # 因为我不是用的嵌套字典，所以这里有细微差别。
    return W


def Recommend(user, dicc, W2, K):
    """
    :param user: 用户
    :param dicc:
    :param W2: 用户兴趣相似度
    :param K: 找到K个相关用户以及对应兴趣相似度，按兴趣相似度从大到小排列
    :return:
    """
    rvi = 1  # 这里都是1,实际中可能每个用户就不一样了。就像每个人都喜欢beautiful girl,但有的喜欢可爱的多一些，有的喜欢御姐多一些。
    rank = dict()
    related_user = []
    interacted_items = dicc[user]
    for co_user, item in W2.items():
        if co_user[0] == user:
            related_user.append((co_user[1], item))  # 先建立一个和待推荐用户兴趣相关的所有的用户列表。
    for v, wuv in sorted(related_user, key=itemgetter(1), reverse=True)[0:K]:
        # 找到K个相关用户以及对应兴趣相似度，按兴趣相似度从大到小排列。itemgetter要导包。
        for i in dicc[v]:
            if i in interacted_items:
                continue  # 书中少了continue这一步吧？
            if i not in rank.keys():  # 如果不写要报错，是不是有更好的方法？
                rank[i] = 0
            rank[i] += wuv * rvi
    return rank


if __name__ == '__main__':
    W3 = Usersim(dic)
    print(W3)
    Last_Rank = Recommend('B', dic, W3, 2)
    print(Last_Rank)
