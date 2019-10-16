# 导包
import redis
from django.http import HttpResponse, HttpResponseRedirect
# 导入类视图
import json
from education import settings
from utils.redis_pool import POOL
from .pay1 import AliPay


# 初始化阿里支付对象
def get_ali_object():
    # 沙箱环境地址：https://openhome.alipay.com/platform/appDaily.htm?tab=info
    app_id = "2016101300676523"  # APPID （沙箱应用）

    # 支付完成后，支付偷偷向这里地址发送一个post请求，识别公网IP,如果是 192.168.20.13局域网IP ,支付宝找不到，def page2() 接收不到这个请求
    # notify_url = "http://127.0.0.1:8000/md_tast/page1_"
    notify_url = settings.MemberPayCallBack

    # 支付完成后，跳转的地址。
    return_url = settings.MemberPayCallBack  # 流水号在这里获取  trade_no
    app_private_key_path = "reception/keys/selfkey.txt"  # 应用私钥
    alipay_public_key_path = "reception/keys/public.txt"  # 支付宝公钥

    alipay = AliPay(
        appid=app_id,
        app_notify_url=notify_url,
        return_url=return_url,
        app_private_key_path=app_private_key_path,
        alipay_public_key_path=alipay_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
        debug=True,  # 默认False,
    )
    return alipay

def get_ali_course_object():
    # 沙箱环境地址：https://openhome.alipay.com/platform/appDaily.htm?tab=info
    app_id = "2016101300676523"  # APPID （沙箱应用）

    # 支付完成后，支付偷偷向这里地址发送一个post请求，识别公网IP,如果是 192.168.20.13局域网IP ,支付宝找不到，def page2() 接收不到这个请求
    # notify_url = "http://127.0.0.1:8000/md_tast/page1_"
    notify_url = settings.CoursePayCallBack

    # 支付完成后，跳转的地址。
    return_url = settings.CoursePayCallBack  # 流水号在这里获取  trade_no
    app_private_key_path = "reception/keys/selfkey.txt"  # 应用私钥
    alipay_public_key_path = "reception/keys/public.txt"  # 支付宝公钥

    alipay = AliPay(
        appid=app_id,
        app_notify_url=notify_url,
        return_url=return_url,
        app_private_key_path=app_private_key_path,
        alipay_public_key_path=alipay_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
        debug=True,  # 默认False,
    )
    return alipay


def page1(request):
    if request.method == "GET":
        # 这个在订单生成成功后，用来获取支付页url，并设置支付页内容
        # 根据当前用户的配置，生成URL，并跳转。
        mes = {}
        memberOrder_sn = request.GET.get('memberOrder_sn')  # 获取订单号
        courseOrder_sn = request.GET.get('courseOrder_sn')  # 获取订单号
        if memberOrder_sn:
            # 通过订单号在redis 中查寻 订单信息
            conn = redis.Redis(connection_pool=POOL)
            order = conn.hget('memberOrder' + str(memberOrder_sn), str(memberOrder_sn))
            order = json.loads(order)
            money = float(order['amount'])
            alipay = get_ali_object()
            # 生成支付的url
            query_params = alipay.direct_pay(
                subject="test",  # 商品简单描述
                out_trade_no=order['order_sn'],  # 用户购买的商品订单号（每次不一样） 20180301073422891
                total_amount=money,  # 交易金额(单位: 元 保留俩位小数)
            )
            pay_url = "https://openapi.alipaydev.com/gateway.do?{0}".format(query_params)  # 支付宝网关地址（沙箱应用）
            mes['code'] = 200
            mes['path'] = pay_url
        elif courseOrder_sn:
            conn = redis.Redis(connection_pool=POOL)
            order = conn.hget('courseOrder' + str(courseOrder_sn), str(courseOrder_sn))
            order = json.loads(order)
            money = float(order['pay_price'])
            alipay = get_ali_course_object()
            # 生成支付的url
            query_params = alipay.direct_pay(
                subject="test",  # 商品简单描述
                out_trade_no=order['order_number'],  # 用户购买的商品订单号（每次不一样） 20180301073422891
                total_amount=money,  # 交易金额(单位: 元 保留俩位小数)

            )
            pay_url = "https://openapi.alipaydev.com/gateway.do?{0}".format(query_params)  # 支付宝网关地址（沙箱应用）
            mes['code'] = 200
            mes['path'] = pay_url

        else:
            mes['code'] = 1000
            mes['message'] = '订单失败'
        return HttpResponse(json.dumps(mes))
