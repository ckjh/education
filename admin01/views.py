from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from admin01.serializer import *


class Userlist(APIView):
    def post(self,request):
        id = request.POST.get('id')
        mes={}
        if id:
            UserLevel.objects.get(id=id).delete()
            mes['code']=200
            mes['msg']="删除成功"
        else:
            mes['code']=400
            mes['msg']="删除失败"
        return Response(mes)
    
    def get(self,request):
        use = UserLevel.objects.all()
        u = UserLevelserializer(use,many=True)
        return Response(u.data)
    