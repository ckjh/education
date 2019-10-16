import requests
import uuid
import json
import redis
import paramiko
import re
import threading
import datetime
from django.shortcuts import render, HttpResponse, redirect
from rest_framework_jwt.settings import api_settings  # jwt中的配置项 api_settings
from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from admin01.serializer import *
from admin01.serializer import CourseSerializersModel
from utils.redis_pool import POOL
from reception.task import *
from utils.captcha.captcha import captcha
from reception.serializers import *
from django.db import transaction
import hashlib


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
        # 激活账号
        ret = {'code': 600, 'message': '激活失败'}
        try:
            token = request.GET.get('token')
            conn = redis.Redis(connection_pool=POOL)

            user = conn.hget('user' + token, token)  # 从redis获取用户
            user = json.loads(user)  # 转成字典
            User.objects.create(email=user['email'], username=user['email'], password=make_password(user['password']),
                                invitation_code=token)
            conn.hdel('user' + token, token)  # 删除原数据
            ret['code'] = 200
            ret['message'] = '激活成功'
            return redirect('http://localhost:8080/#/?code=' + ret['message'])
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
        return Response(res)

    def post(self, request):
        ret = {}
        username = request.data['username']
        password = request.data['password']
        uid = request.data.get("uid")
        user = User.objects.filter(email=username).first()
        print(user.username)

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
                    user = User.objects.filter(email=username).first()
                    ThirdPartyLogin.objects.create(user_id=user.id, uid=uid, type=1)
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
        print(ret)
        return Response(ret)


class ShowCoursesAPIView(APIView):
    def get(self, request):  # 展示课程
        ret = {}
        sale = request.GET.get('sale')
        tag = request.GET.get('tag')
        member = request.GET.get('member')
        sort = request.GET.get('sort')  # sort 排序方式 其中 create_time 最新,learn 最热
        searchDict = {}
        if sale != '-1': searchDict['online'] = sale  # 是否上线 -1 是未勾选，0未上线，1 已上线；
        if tag != '-1': searchDict['tag'] = tag  # 标签id -1是全部
        if member != '-1': searchDict['member'] = member  # member 是否为会员课程，0 否 1 是 -1 全部
        try:
            dataList = Course.objects.filter(**searchDict).order_by(sort)
            dataList = CourseSerializersModel(dataList, many=True)
            ret['dataList'] = dataList.data
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as ex:
            print(ex)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)


class PathDetailAPIView(APIView):
    def get(self, request):
        ret = {}
        id = request.GET.get('id')
        print(id)
        path = Path.objects.get(id=id)
        print(path)
        path = PathSerializersModel(path, many=False)
        ret['pathData'] = path.data
        ret['code'] = 200
        ret['message'] = '成功'
        print(ret)
        return Response(ret)


from dwebsocket import accept_websocket

host = settings.IP
username = settings.USER
password = settings.PASSWORD


def _ssh(host, username, password, port=22):
    sh = paramiko.SSHClient()
    sh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sh.connect(host, username=username, password=password)
    channle = sh.invoke_shell(term='xterm')
    return channle


def recv_ssh_msg(channle, ws):
    '''
        channle: 建立好的SSH连接通道
        这个函数会不停的接收ssh通道返回的命令
        返回到前端的ws套接字里
    '''
    while not channle.exit_status_ready():
        try:
            buf = channle.recv(1024)  # 接收 蓝色
            ws.send(buf)  # 巧克力色
        except:
            break


@accept_websocket
def webssh(request):
    ''' 1: 接收前端(ws)的命令，发给后台(ssh)
    2: 接收后台的返回结果，给到前端 '''
    if request.is_websocket:
        channle = _ssh(host, username=username, password=password)
        ws = request.websocket
        t = threading.Thread(target=recv_ssh_msg, args=(channle, ws))
        t.setDaemon(True)
        t.start()  # 线程开启
        while 1:
            cmd = ws.wait()  # 阻塞接收前端发来的命令
            if cmd:
                channle.send(cmd)  # 由SSH通道转交给Linux环境
            else:  # 连接断开 跳出循环
                break
            ws.close()  # 释放对应套接字资源
            channle.close()


# 加入路径
class MyPath(APIView):
    def post(self, request):
        path_id = request.data['path_id']
        user_id = request.data['user_id']
        u = UserPath.objects.filter(path_id=path_id, user_id=user_id).first()
        mes = {}
        if u:  # 存在即删除
            UserPath.objects.filter(path_id=path_id, user_id=user_id).delete()
            mes['code'] = 201
            mes['message'] = '取消路径成功!'
        else:
            try:
                UserPath.objects.create(path_id=path_id, user_id=user_id)
                mes['code'] = 200
                mes['message'] = '已加入我的路径,可在用户中心查看!'
            except:
                mes['code'] = 10010
                mes['message'] = '数据发生错误'
        return Response(mes)


# 我的优惠券
class MyCoupon(APIView):
    def get(self, request):
        user_id = request.GET.get('user_id')
        mes = {}

        if user_id:
            u = Usercoupon.objects.filter(user_id=user_id).all()
            usercoupon = UserCouponModelSerializer(u, many=True)
            mes['code'] = 200
            mes['couponList'] = usercoupon.data
            mes['message'] = 'ok'
        else:
            mes['code'] = 10010
            mes['message'] = '用户id不存在请登录'

        return Response(mes)

    def post(self, request):
        data = request.data.copy()
        mes = {}
        user_id = request.data['user_id']  # 用户id
        coupon_id = request.data['coupon_id']  # 优惠券id
        code = hashlib.md5(
            str('user' + str(user_id) + 'coupon' + str(coupon_id)).encode(
                'utf-8')).hexdigest()  # 当该用户和同一优惠券搭配时生成相同的数据指纹
        myCoupon = Usercoupon.objects.filter(code=code)  # 根据code 码判断用户是否已经领取
        if myCoupon:
            mes['code'] = 10010
            mes['message'] = '领取失败'
            return Response(mes)
        data['code'] = code
        coupon = Coupon.objects.filter(id=coupon_id).first()
        user = Member.objects.get(user_id=user_id)
        data['start_time'] = datetime.datetime.now()
        data['end_time'] = datetime.datetime.now()
        data['money'] = coupon.money
        data['type'] = coupon.type
        data['condition'] = coupon.condition
        data['is_use'] = coupon.status
        if coupon.count > 1 and coupon.status == 1:
            if coupon.type == 1 and user:  # 首次开通会员领取
                u = UserCouponSerializer(data=data)
                if u.is_valid():
                    u.save()
                    mes['code'] = 200
                    mes['message'] = '领取成功'
                else:
                    print(u.errors)
                    mes['code'] = 10010
                    mes['message'] = '领取失败'
            elif coupon.type == 2:
                u = UserCouponSerializer(data=data)
                if u.is_valid():
                    u.save()
                    mes['code'] = 200
                    mes['message'] = '领取成功'
                else:
                    print(u.errors)
                    mes['code'] = 10010
                    mes['message'] = '领取失败'
            elif coupon.type == 3:
                data['cid'] = coupon.id
                u = UserCouponSerializer(data=data)
                if u.is_valid():
                    u.save()
                    mes['code'] = 200
                    mes['message'] = '领取成功'
                else:
                    print(u.errors)
                    mes['code'] = 10010
                    mes['message'] = '领取失败'

            else:
                u = UserCouponSerializer(data=data)
                if u.is_valid():
                    u.save()
                    mes['code'] = 200
                    mes['message'] = '领取成功'
                else:
                    print(u.errors)
                    mes['code'] = 10010
                    mes['message'] = '领取失败'
        else:
            mes['code'] = 10010
            mes['message'] = '优惠券数量不够'
        if mes['code'] == 200:
            coupon.count -= 1
            coupon.save()
        return Response(mes)


class UserInfoAPIView(APIView):
    def get(self, request):
        ret = {}
        user_id = request.GET.get('user_id')
        print(user_id)
        user = User.objects.get(id=user_id)
        user = UserSerializersModel(user)
        ret['userInfo'] = user.data
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)


class MemberOrderAPIView(APIView):
    def get(self, request):
        # 支付成功立即自动回调这个借口,会传回几个参数,其中我们取出订单号,流水号
        order_sn = request.GET.get('out_trade_no')  # 订单号
        trade_no = request.GET.get('trade_no')  # 流水号
        print(trade_no)
        # 将存在redis中的订单使用订单号读出
        ret = {}
        conn = redis.Redis(connection_pool=POOL)
        order = conn.hget('memberOrder' + str(order_sn), str(order_sn))
        order = json.loads(order).copy()
        # 完善订单信息存入memberOrder表
        order['code'] = trade_no
        order['status'] = 1  # 将订单状态改为 已支付
        print(order)
        o = MemberOrderSerializer(data=order)
        # 更新积分:首先用户是否使用积分要判断
        if o.is_valid():
            o.save()
            user = User.objects.get(id=int(order['user_id']))
            user.level_id = int(order['level_id'])
            user.save()
            # 判断用户是否使用邀请码
            if order['invitation_code'] != '':
                # 为邀请者加积分,通过邀请码找到邀请者
                invitationUser = User.objects.filter(invitation_code=order['invitation_code']).first()
                invitationUser.integral += 100
                invitationUser.save()
            d1 = datetime.datetime.now()
            # 计算过期时间
            d3 = d1 + datetime.timedelta(days=31 * int(order['time']))
            # 向维护会员过期时间的表中添加数据
            Member.objects.create(user_id=int(order['user_id']), level_id=int(order['level_id']), start_time=d1,
                                  end_time=d3)
            ret['code'] = 200
            ret['message'] = '成功'
        else:
            user = User.objects.get(id=int(order['user_id']))
            user.integral += int(order['num'])
            print(o.errors)
            ret['code'] = 1000
            ret['message'] = '失败'
        return redirect(settings.UserCenterUrl)

    def post(self, request):
        # 在支付前生成会员订单时调用
        ret = {}
        data = request.data.copy()
        # 验证获取的数据
        level = UserLevelCondition.objects.filter(level_id=data['level_id']).first()  # 获取等级条件
        user = User.objects.get(id=data['user_id'])  # 获取用户信息
        rule = Rule.objects.first()  # 获取抵扣比例
        member = Member.objects.filter(user_id=int(data['user_id']))
        # 判断用户是否为会员,如果已经开通那就返回失败
        if member:
            ret['code'] = 1000
            ret['message'] = '您已成为会员'
            return Response(ret)
        # 判断用户是否输入邀请码
        if data['invitation_code'] == '':
            invitationUser = True
            # 定义为True以通过下面的判断
        else:  # 如果输入了,去用户表找邀请者
            invitationUser = User.objects.filter(invitation_code=data['invitation_code']).first()
            if invitationUser.id != user.id:
                invitationUser = False
        # 判断用户输入,等级信息,邀请者信息是否正确
        if user.integral > int(data['num']) and level and invitationUser and float(
                level.amount - rule.ratio * int(data['num'])) > 0:
            # float(level.amount - rule.ratio * int(data['num'])) > 0,积分用的太多导致价格成了负数
            # user.integral > int(data['num']) 判断用户使用的积分是否比自己拥有的多,防止花超了
            # level 判断用户等级是否存在
            # invitationUser判断用户输入的邀请码是否有对应的邀请者
            # invitationUser.id != user.id 判断用户是否在用自己的邀请码开会员，这是典型的刷分操作
            # 以上任何一种错误都不能存现
            data['time'] = level.time  # 通过用户等级条件表获取开通时限
            data['amount'] = float(level.amount - rule.ratio * int(data['num']))  # 实际花的钱
            # 实际花费 = 原价 - 抵扣比例 * 积分
            data['order_sn'] = str(uuid.uuid1()).replace('-', '')  # 订单号
            # 将订单信息存入redis
            conn = redis.Redis(connection_pool=POOL)
            conn.hset('memberOrder' + data['order_sn'], data['order_sn'], json.dumps(data))
            conn.expire('memberOrder' + data['order_sn'], 600)  # 设置过期时间未600秒,就是 600秒内不支付 订单消失
            if int(data['num']) > 0:
                # 如果使用了,那减去相应积分
                user.integral -= int(data['num'])
                user.save()
                # 判断用户是否使用邀请码
            ret['order_sn'] = data['order_sn']  # 将订单号作为响应内容传回页面，根据该订单号以获取支付页面的url，逻辑在pay.py
            ret['code'] = 200
            ret['message'] = '成功'
        else:  # 用户输入的信息有误
            ret['code'] = 1000
            ret['message'] = '失败'
        return Response(ret)

    def put(self, request):
        mes = {}
        try:
            data = request.data.copy()
            c1 = MemberOrder.objects.filter(user_id=data['user_id']).all()
            ser = MemberOrderSerializersModel(c1, many=True)
            mes['dataList'] = ser.data
            mes['code'] = 200
            mes['msg'] = 'ok'
        except:
            mes['code'] = 10010
            mes['message'] = '失败'
        return Response(mes)


class OrderRecordAPIView(APIView):
    def get(self, request):
        ret = {}
        order_sn = request.GET.get('out_trade_no')  # 订单号
        trade_no = request.GET.get('trade_no')  # 流水号
        print(trade_no)
        # 将存在redis中的订单使用订单号读出
        conn = redis.Redis(connection_pool=POOL)
        order = conn.hget('courseOrder' + str(order_sn), str(order_sn))
        order = json.loads(order).copy()
        # 完善订单信息存入memberOrder表
        order['code'] = trade_no
        order['order_status'] = 1  # 将订单状态改为 已支付
        order['user_id']=order['uid']
        order['course_id']=order['cid']
        o = CourseOrderSerializer(data=order)
        if o.is_valid():
            o.save()
            ret['code'] = 200
            ret['message'] = '成功'
        else:
            user = User.objects.get(id=int(order['uid']))
            user.integral += int(order['num'])
            print(o.errors)
            ret['code'] = 1000
            ret['message'] = '失败'
        return Response(ret)

    def post(self, request):
        ret = {}
        data = request.data.copy()
        print(data)
        user = User.objects.get(id=data['uid'])  # 用户
        course = Course.objects.get(id=data['cid'])  # 课程
        coupon = Usercoupon.objects.filter(code=data['coupon']).first()
        rule = Rule.objects.first()
        print(course, user, coupon)
        if user and course and int(data['preferential_way']) in [0, 1, 3]:
            price = Price.objects.filter(type=user.level_id).first().discoun_price  # 课程原价
            data['price'] = price
            # 未选优惠方式
            if int(data['preferential_way']) == 0:
                data['coupon'], data['num'], data['preferential_money'] = '', 0, 0
                data['pay_price'] = price
            # 选择用优惠券
            elif int(data['preferential_way']) == 1:
                data['num'] = 0
                idList = [0, course.id]  # 如果不是制定课程的id 或是 未指定课程均为优惠券误用
                c = Coupon.objects.filter(id=coupon.cid).first()
                if coupon.condition > price or c.course not in idList:
                    ret['code'] = 601
                    ret['message'] = '优惠信息错误'
                    return Response(ret)
                data['pay_price'] = price - coupon.money
                data['preferential_money'] = coupon.money
            # 选择用积分
            elif int(data['preferential_way']) == 2:
                data['coupon'] = ''
                if price < int(rule.ratio * data['num']) or user.integral < int(data['num']):
                    ret['code'] = 601
                    ret['message'] = '优惠信息错误'
                    return Response(ret)
                data['preferential_money'] = rule.ratio * data['num']
                data['pay_price'] = price - rule.ratio * data['num']
            else:
                ret['code'] = 601
                ret['message'] = '优惠方式错误'
                return Response(ret)
                # 订单号
            data['order_number'] = str(uuid.uuid1()).replace('-', '')
            ret['code'] = 200
            ret['message'] = '成功'
            print(data)
            data['price'] = float(data['price'])
            data['preferential_money'] = float(data['preferential_money'])
            data['pay_price'] = float(data['pay_price'])
            conn = redis.Redis(connection_pool=POOL)
            conn.hset('courseOrder' + data['order_number'], data['order_number'], json.dumps(data))
            conn.expire('courseOrder' + data['order_number'], 600)  # 设置过期时间未600秒,就是 600秒内不支付 订单消失
        else:
            ret['code'] = 1000
            ret['order_number'] = data['order_number']
            ret['message'] = "订单信息错误"

        return Response(ret)
