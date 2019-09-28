from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from admin01.serializer import *
from django.core.paginator import Paginator


# 用户等级管理
class LevelAPIView(APIView):
    def post(self, request):  # 添加等级
        ret = {}
        try:
            data = request.data
            UserLevel.objects.create(level=data['level'])
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def delete(self, request):  # 删除等级
        ret = {}
        try:
            data = request.data
            UserLevel.objects.get(id=data['id']).delete()
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def put(self, request):  # 修改等级
        ret = {}
        try:
            data = request.data
            obj = UserLevel.objects.get(id=data['id'])
            obj.level = data['level']
            obj.save()
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def get(self, request):  # 展示标签
        ret = {}
        levels = UserLevel.objects.all()
        levels = UserLevelSerializer(levels, many=True)
        ret['levels'] = levels.data
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)


# 课程标签管理
class TagAPIView(APIView):
    def post(self, request):  # 添加标签
        ret = {}
        try:
            data = request.data
            print(data)
            Tag.objects.create(name=data['name'])
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def delete(self, request):  # 删除标签
        ret = {}
        try:
            data = request.data
            Tag.objects.get(id=data['id']).delete()
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def put(self, request):  # 修改标签
        ret = {}
        try:
            data = request.data
            obj = Tag.objects.get(id=data['id'])
            obj.name = data['name']
            obj.save()
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def get(self, request):  # 展示标签
        ret = {}
        try:
            tags = Tag.objects.all()
            tags = TagSerializersModel(tags, many=True)
            ret['tags'] = tags.data
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as ex:
            print(ex)
            ret['code'] = 601
            ret['message'] = '数据库错误'

        return Response(ret)


# 用户等级条件管理
class ConditionAPIView(APIView):
    def post(self, request):  # 添加用户等级条件 参数 id ,level_id ,amount, time
        mes = {}
        try:
            ser = UserLevelConditionSerializers(data=request.data)
            if ser.is_valid():
                ser.save()
                mes['code'] = 200
                mes['message'] = '成功'
                mes['data'] = ser.data
            else:
                print(ser.errors)
                mes['code'] = 601
                mes['message'] = '失败'
        except Exception as ex:
            print(ex)
            mes['code'] = 601
            mes['message'] = '数据库错误'
        return Response(mes)

    def delete(self, request):  # 删除条件
        ret = {}
        try:
            data = request.data
            UserLevelCondition.objects.get(id=data['id']).delete()
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def put(self, request):  # 修改条件 参数 id ,level_id ,amount, time
        mes = {}
        try:
            id = request.data['id']
            c1 = UserLevelCondition.objects.get(id=id)
            ser = UserLevelConditionSerializers(c1, data=request.data)
            if ser.is_valid():
                ser.save()
                mes['code'] = 200
                mes['message'] = '成功'
                mes['data'] = ser.data
            else:
                print(ser.errors)
                mes['code'] = 601
                mes['message'] = '失败'
        except Exception as es:
            mes['code'] = 601
            mes['message'] = '数据库错误'
        return Response(mes)

    def get(self, request):
        ret = {}
        try:
            p = request.GET.get('p')
            conditions = UserLevelCondition.objects.all()
            paginator = Paginator(conditions, 2)
            conditions = paginator.page(int(p))
            conditions = ConditionSerializersModel(conditions, many=True)
            ret['conditions'] = conditions.data
            ret['currentPage'] = p
            ret['totalPage'] = paginator.num_pages
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as ex:
            print(ex)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)
