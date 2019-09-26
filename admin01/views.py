from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from admin01.serializer import *


class Userlist(APIView):
    def post(self, request):
        id = request.POST.get('id')
        mes = {}
        if id:
            UserLevel.objects.get(id=id).delete()
            mes['code'] = 200
            mes['msg'] = "删除成功"
        else:
            mes['code'] = 400
            mes['msg'] = "删除失败"
        return Response(mes)

    def get(self, request):
        use = UserLevel.objects.all()
        u = UserLevelserializer(use, many=True)
        return Response(u.data)





class ShowCondition(APIView):
    def get(self, request):
        ret = {}
        try:
            conditions = UserLevelCondition.objects.all()
            conditions = ConditionSerializersModel(conditions, many=True)
            ret['conditions'] = conditions.data
            ret['code'] = 200
            ret['message'] = '成功'
        except:
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)


class DeleteCondition(APIView):
    def get(self, request):
        ret = {}
        try:
            id = request.GET.get('id')
            UserLevelCondition.objects.get(id=id).delete()
            ret['code'] = 200
            ret['message'] = '成功'
        except:
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)


class Level(APIView):
    def post(self, request):
        ser = LevelSerializer(data=request.data)
        mes = {}
        if ser.is_valid():
            ser.save()
            mes['code'] = 200
            mes['message'] = '成功'
            mes['data'] = ser.data
        else:
            print(ser.errors)
            mes['code'] = 400
            mes['message'] = '失败'
        return Response(mes)

    def put(self, request):  # todo 修改
        content = request.data
        id = int(content['id'])                           # 获取点击后的内容id
        c1 = UserLevel.objects.get(id=id)
        c = LevelSerializer(c1, data=content)

        mes = {}
        if c.is_valid():
            c.save()
            mes['code'] = 200
            mes['message'] = 'ok'
        else:
            print(c.errors)
            mes['code'] = 10020
            mes['message'] = '失败'
        return Response(mes)
