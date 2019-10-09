from django.shortcuts import render
import os
import paramiko
from uuid import uuid1
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from reception.task import send
class SendMailAPIView(APIView):
    def get(self, request):
        ret = {}
        send.delay('liguilin_L@163.com')
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)
