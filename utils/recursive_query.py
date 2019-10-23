from utils.mongo_pool import client
from admin01.models import *
import pymongo


def sub_comment(course):
    db = client['dbdb']
    print(course)
    comm = db['comment']
    c = comm.find({'course_id': course}).sort(
        [("create_time", pymongo.DESCENDING)])  # 获取 本课程下 的所有评论 根据时间排序 及审核通过的
    list = []

    for i in c:
        dic = {}
        user_id = i['user_id']
        u = User.objects.get(id=user_id)
        m = Member.objects.get(user_id=u.id)
        s = UserLevel.objects.get(id=m.level_id)
        dic['username'] = u.username
        dic['img'] = u.img
        dic['userlevel'] = s.level
        dic['_id'] = i['_id']
        dic['content'] = i['content']
        dic['pid'] = i['pid']
        dic['top_id'] = i['top_id']
        dic['type'] = i['type']
        dic['user_id'] = i['user_id']
        dic['course_id'] = i['course_id']
        dic['status'] = i['status']
        dic['create_time'] = i['create_time']
        try:
            dic['back_username'] = i['username']
        except:
            dic['back_username'] = ''
        list.append(dic)
    return list
    # return []


def sub_commentdetail(course):
    db = client['dbdb']
    comm = db['discomment']
    c = comm.find({'diss_id': int(course), 'status': 1}).sort([("create_time", pymongo.DESCENDING)])
    list = []
    if c:
        for i in c:
            dic = {}
            user_id = i['user_id']
            u = User.objects.get(id=user_id)
            m = Member.objects.get(user_id=u.id)
            s = UserLevel.objects.get(id=m.level_id)
            dic['username'] = u.username
            dic['img'] = u.img
            dic['userlevel'] = s.level
            dic['_id'] = i['_id']
            dic['content'] = i['content']
            dic['pid'] = i['pid']
            dic['top_id'] = i['top_id']
            dic['type'] = i['type']
            dic['user_id'] = i['user_id']
            # dic['title'] = i['title']
            dic['status'] = i['status']
            dic['create_time'] = i['create_time']
            try:
                dic['back_username'] = i['username']
            except:
                dic['back_username'] = ''
            list.append(dic)
        return list
    return []


def sub_dissdetail(course):
    db = client['dbdb']
    comm = db['discomment']
    c = comm.find({'_id': int(course), 'status': 1}).sort([("create_time", pymongo.DESCENDING)])
    list = []
    if c:
        for i in c:
            dic = {}
            user_id = i['user_id']
            u = User.objects.get(id=user_id)
            m = Member.objects.get(user_id=u.id)
            s = UserLevel.objects.get(id=m.level_id)
            dic['username'] = u.username
            dic['img'] = u.img
            dic['userlevel'] = s.level
            dic['_id'] = i['_id']
            dic['content'] = i['content']
            dic['pid'] = i['pid']
            dic['top_id'] = i['top_id']
            dic['type'] = i['type']
            dic['user_id'] = i['user_id']
            dic['title'] = i['title']
            dic['status'] = i['status']
            dic['create_time'] = i['create_time']
            try:
                dic['back_username'] = i['username']
            except:
                dic['back_username'] = ''
            list.append(dic)
        return list
    return []


def sub_sscomment(course):
    db = client['dbdb']
    comm = db['discomment']
    c = comm.find({'types': int(course), 'status': 1}).sort(
        [("create_time", pymongo.DESCENDING)])  # 获取 本课程下 的所有评论 根据时间排序 及审核通过的
    list = []
    if c:
        for i in c:
            dic = {}
            user_id = i['user_id']
            u = User.objects.get(id=user_id)
            m = Member.objects.get(user_id=u.id)
            s = UserLevel.objects.get(id=m.level_id)
            dic['username'] = u.username
            dic['img'] = u.img
            dic['userlevel'] = s.level
            dic['_id'] = i['_id']
            dic['content'] = i['content']
            dic['pid'] = i['pid']
            dic['top_id'] = i['top_id']
            dic['type'] = i['type']
            dic['user_id'] = i['user_id']
            dic['title'] = i['title']
            dic['status'] = i['status']
            dic['create_time'] = i['create_time']
            try:
                dic['back_username'] = i['username']
            except:
                dic['back_username'] = ''
            list.append(dic)
        return list
    return []


def sub_questdetail(quest_id):
    print(quest_id, '报告搜索', type(quest_id))
    db = client['dbdb']
    comm = db['comment']
    c = comm.find({'quest_id': quest_id, 'status': 1}).sort([("create_time", pymongo.DESCENDING)])
    list = []
    for i in c:
        print(i)
        dic = {}
        user_id = i['user_id']
        u = User.objects.get(id=user_id)
        m = Member.objects.get(user_id=u.id)
        s = UserLevel.objects.get(id=m.level_id)
        dic['username'] = u.username
        dic['img'] = u.img
        dic['userlevel'] = s.level
        dic['_id'] = i['_id']
        dic['content'] = i['content']
        dic['pid'] = i['pid']
        dic['top_id'] = i['top_id']
        dic['type'] = i['type']
        dic['user_id'] = i['user_id']
        # dic['title'] = i['title']
        dic['status'] = i['status']
        dic['create_time'] = i['create_time']
        try:
            dic['back_username'] = i['username']
        except:
            dic['back_username'] = ''
        list.append(dic)
    return list


def sub_usercomment(course):
    db = client['dbdb']
    comm = db['discomment']
    c = comm.find({'user_id': str(course), 'types': 1, 'status': 1}).sort(
        [("create_time", pymongo.DESCENDING)])  # 获取 本课程下 的所有评论 根据时间排序 及审核通过的
    list = []
    if c:
        for i in c:
            dic = {}
            print(i)
            user_id = i['user_id']
            u = User.objects.get(id=user_id)
            m = Member.objects.get(user_id=u.id)
            s = UserLevel.objects.get(id=m.level_id)
            dic['username'] = u.username
            dic['img'] = u.img
            dic['userlevel'] = s.level
            dic['_id'] = i['_id']
            dic['content'] = i['content']
            dic['pid'] = i['pid']
            dic['top_id'] = i['top_id']
            dic['type'] = i['type']
            dic['user_id'] = i['user_id']
            dic['title'] = i['title']
            dic['status'] = i['status']
            dic['create_time'] = i['create_time']
            try:
                dic['back_username'] = i['username']
            except:
                dic['back_username'] = ''
            list.append(dic)
        return list
    return []
