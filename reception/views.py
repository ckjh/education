import requests
from django.shortcuts import render, HttpResponse, redirect
from rest_framework_jwt.settings import api_settings  # jwt中的配置项 api_settings
from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.redis_pool import POOL
from reception.task import *
from utils.captcha.captcha import captcha
from admin01.models import *
import uuid
import json
import redis
import paramiko
import re


# 验证码 获取文本
def GetImageCode(request):
    name, text, image = captcha.generate_captcha()
    # 存入session 用户提交的时候进行对比
    request.session['image_code'] = text
    return HttpResponse(image, 'image/png')


# 注册接口
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
                    ret['code'] = 10040
                    ret['message'] = '验证码输入错误'
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
        username = request.data['username']
        password = request.data['password']
        print(password)
        user = User.objects.filter(username=username).first()
        res = {}
        if check_password(password, user.password):  # 查找用户 比对密码
            if user.integral == 1:  # 如果未激活
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

    def get(self, request):
        # 重定向到微博登陆
        # 回调网址
        # 应用id
        client_id = settings.APP_KEY
        url = "https://api.weibo.com/oauth2/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_url}".format(
            client_id=client_id, redirect_url=settings.CALLBACK_URL)
        return redirect(url)


# 忘记密码
class ForGetPwd(APIView):
    def post(self, request):
        mes = {}
        email = request.data['email']
        image_code = request.data['image_code']
        if re.match("^[a-z0-9A-Z]+[-|a-z0-9A-Z._]+@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\\.)+[a-z]{2,}$", email):  # 判断邮箱正确性
            if image_code == request.session.get('image_code').lower():
                try:
                    uid = User.objects.filter(email=email).first()
                    send1.delay(uid=uid, email=email)
                    mes['code'] = 200
                    mes['message'] = '发送邮件成功'
                except:
                    mes['code'] = 10030
                    mes['message'] = '未注册无效用户'
            else:
                mes['code'] = 10010
                mes['message'] = '验证码错误'
        else:
            mes['code'] = 10020
            mes['message'] = '邮箱格式错误'

        return Response(mes)


class ThirdPartAPIView(APIView):
    def put(self, request):
        ret = {}
        # 获取回调的code
        code = request.data['code']
        # 微博认证地址
        access_token_url = "https://api.weibo.com/oauth2/access_token"
        # 参数
        response = requests.post(access_token_url, data={
            "client_id": settings.APP_KEY,
            "client_secret": settings.APP_SECRET,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": settings.CALLBACK_URL,
        })
        res = response.text
        res = eval(str(res))
        print(res)
        uid = res.get('uid')
        u = ThirdPartyLogin.objects.filter(uid=uid).first()
        if u:
            user = User.objects.get(id=u.user_id)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)  # 用户对象 处理器
            # 通过jwt编码 生成token令牌
            token = jwt_encode_handler(payload)
            res["code"] = 200
            res["token"] = token  # 自定义登录生成token
            res["uid"] = user.id
            res["username"] = user.username
            res['message'] = '登录成功'
        else:
            res['uid'] = uid
            res["code"] = 600
            res['message'] = '未绑定本平台账号'
        return Response(ret)

    def post(self, request):
        ret = {}
        username = request.data.get("username")
        password = request.data.get("password")
        uid = request.data.get("uid")
        print(username, password)
        user = User.objects.filter(username=username).first()
        # 判断用户是否存在
        if user:
            # 如果存在就去验证密码绑定
            if user and user.check_password(password):  # 查找用户 比对密码
                ThirdPartyLogin.objects.create(user_id=user.id, uid=uid, type=1)
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)  # 用户对象 处理器
                # 通过jwt编码 生成token令牌
                token = jwt_encode_handler(payload)
                ret["token"] = token  # 自定义登录生成token
                ret["uid"] = user.id
                ret["username"] = username
                ret['code'] = 200
                ret['message'] = '绑定并登陆成功'
            else:
                # 密码不对绑定失败
                ret['code'] = 601
                ret['message'] = '绑定失败'

        else:
            # 如果用户名不存在,从新注册
            if re.match("^[a-z0-9A-Z]+[-|a-z0-9A-Z._]+@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\\.)+[a-z]{2,}$",
                        username):  # 判断邮箱正确性
                if 18 >= len(password) >= 6:  # 判断密码
                    User.objects.create(email=username, username=username,
                                        password=make_password(password))
                    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                    payload = jwt_payload_handler(user)  # 用户对象 处理器
                    # 通过jwt编码 生成token令牌
                    token = jwt_encode_handler(payload)
                    ret["token"] = token  # 自定义登录生成token
                    ret["uid"] = user.id
                    ret["username"] = username
                    ret['code'] = 200
                    ret['message'] = '绑定注册登陆成功'
                else:
                    # 用户名密码输入不合法就失败
                    ret['code'] = 601
                    ret['message'] = '绑定失败'
        return Response(ret)

    def get(self, request):
        ret = {}
        code = request.GET.get('code')
        ret['code'] = 200
        ret['message'] = '成功'
        return redirect('http://127.0.0.1:8080/#/weibo_callback/?code=' + code)
