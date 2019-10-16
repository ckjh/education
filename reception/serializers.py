from rest_framework import serializers
from admin01.models import *


# 我的优惠券序列化
class UserCouponModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usercoupon
        fields = '__all__'


# 用户优惠券反序列化类
class UserCouponSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    type = serializers.IntegerField()
    code = serializers.CharField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    money = serializers.DecimalField(max_digits=7, decimal_places=2)
    condition = serializers.DecimalField(max_digits=7, decimal_places=2)  # 满减
    is_use = serializers.IntegerField()  # 0未使用，1使用

    def create(self, data):
        usercoupon = Usercoupon.objects.create(**data)
        return usercoupon


# 维护会员过期时间的表序列化类

class MemberSerializersModel(serializers.ModelSerializer):
    level_name = serializers.CharField(source='level.level')

    class Meta:
        model = Member
        fields = '__all__'


# 用户表序列化类

class UserSerializersModel(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()

    # 序列化类嵌套获取用户会员状态信息
    def get_level(self, row):
        try:
            member = Member.objects.filter(user_id=row.id).first()
            member = MemberSerializersModel(member, many=False)
            return member.data
        except Exception as e:

            return {}

    class Meta:
        model = User
        fields = '__all__'


# 会员订单序列化类
class MemberOrderSerializersModel(serializers.ModelSerializer):
    level_name = serializers.CharField(source='level.level')

    class Meta:
        model = MemberOrder
        fields = '__all__'


# 会员订单反序列化类
class MemberOrderSerializer(serializers.Serializer):
    order_sn = serializers.CharField(max_length=100)
    user_id = serializers.IntegerField()
    level_id = serializers.IntegerField()
    time = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=7, decimal_places=2)  # 支付金额
    pay_type = serializers.IntegerField()  # 支付方式
    invitation_code = serializers.CharField(default='')  # 邀请码

    class Meta:
        db_table = MemberOrder

    def create(self, data):
        m = MemberOrder.objects.create(**data)
        return m
