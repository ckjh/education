from django.shortcuts import render,HttpResponse
from rest_framework_jwt.settings import api_settings  # jwt中的配置项 api_settings
from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.redis_pool import POOL
from reception.task import send
from utils.captcha.captcha import captcha
from admin01.models import *
import uuid
import json
import redis
import paramiko
import re



# 验证码 获取文本
def GetImageCode(request):
    name,text,image = captcha.generate_captcha()
    #存入session 用户提交的时候进行对比
    request.session['image_code'] = text
    print(name)
    print(text)
    print(image)
    return HttpResponse(image,'image/png')


#注册接口
class RegAPIView(APIView):
    def post(self, request):
        ret = {}
        data = request.data
        image_code = data['image_code']
        cartDict = {}
        if re.match("^[a-z0-9A-Z]+[-|a-z0-9A-Z._]+@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\\.)+[a-z]{2,}$",
                    data['email']):  # 判断邮箱正确性
            if 18 >= len(data['password']) >= 6:  # 判断密码
                # 获取session验证文本
                image_code1 = request.session.get('image_code').lower()
                if image_code == image_code1:
                    # 建立reids连接
                    conn = redis.Redis(connection_pool=POOL)
                    # 生成 token
                    token = str(uuid.uuid1()).replace('-', '')
                    cartDict['email'] = data['email']
                    cartDict['password'] = data['password']
                    #  存入 reids ==> user:表名  token: 键  cartDict: 值
                    conn.hset('user' + token, token, json.dumps(cartDict))
                    conn.expire('user' + token, 2592000)  # 设置过期时间一个月
                    # 发送邮箱 激活账户
                    send.delay(token=token, email=data['email'])
                    ret['code'] = 200
                    ret['message'] = '成功'
                else:
                    ret[ 'code' ] = 10040
                    ret[ 'message' ] = '验证码输入错误'
            else:
                ret['code'] = 10010
                ret['message'] = '密码长度小于6位大于18位'
        else:
            ret['code'] = 10020
            ret['message'] = '邮箱格式不正确'
        return Response(ret)

    def get(self, request):
        ret = {'code': 600, 'message': '激活失败'}
        try:
            token = request.GET.get('token')
            conn = redis.Redis(connection_pool=POOL)
            # conn.hgetall()
            user = conn.hget('user' + token, token)  # 从redis获取用户
            user = json.loads(user)  # 转成字典
            User.objects.create(email=user['email'], username=user['email'], password=make_password(user['password']))
            conn.hdel('user' + token, token)  # 删除原数据
            ret['code'] = 200
            ret['message'] = '激活成功'
        except Exception as e:
            print(e)
        return Response(ret)


class LoginAPIView(APIView):  # todo 登录
    def post(self, request):  # 登录的时候需要 验证码 账号与密码  验证通过 返回令牌 用户的个人信息
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.filter(username=username).first()
        res = {}
        if user and user.check_password(password):  # 查找用户 比对密码
            if user.is_valide == 1:  # 如果未激活
                res["code"] = 301
                res["msg"] = "用户未在激活状态"
            else:  # 激活了   提供令牌 作为 登录成功的标识
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)  # 用户对象 处理器
                # 通过jwt编码 生成token令牌
                token = jwt_encode_handler(payload)

                res["code"] = 200
                res["token"] = token  # 自定义登录生成token
                res["uid"] = user.id
                res["username"] = username
                res['meg'] = '登录成功'
        else:  # 没有 找到用户 或密码错误
            res["code"] = 401
            res["msg"] = "用户名或密码错误"
        return Response(res)
