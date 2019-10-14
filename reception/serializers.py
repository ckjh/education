from rest_framework import serializers
from admin01.models import *


# 我的优惠券序列化
class UserCouponModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usercoupon
        fields = '__all__'


class UserCouponSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    type = serializers.IntegerField()
    code = serializers.CharField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    money = serializers.DecimalField(max_digits=7, decimal_places=2)
    condition = serializers.DecimalField(max_digits=7, decimal_places=2)
    is_use = serializers.IntegerField()  # 0未使用，1使用

    class Meta:
        db_table = 'usercoupon'

    def create(self, data):
        usercoupon = Usercoupon.objects.create(**data)
        return usercoupon


class MemberSerializersModel(serializers.ModelSerializer):
    level_name = serializers.CharField(source='level.level')

    class Meta:
        model = Member
        fields = '__all__'


class UserSerializersModel(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()

    def get_level(self, row):
        try:
            member = Member.objects.filter(user_id=row.id).first()
            member = MemberSerializersModel(member, many=False)
            return member.data
        except Exception as e:

            return str(e)

    class Meta:
        model = User
        fields = '__all__'
