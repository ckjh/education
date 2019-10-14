from rest_framework import serializers
from admin01.models import *

#我的优惠券序列化
class UserCouponModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usercoupon
        fields = '__all__'


class UserCouponSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    type = serializers.IntegerField()
    code = serializers.IntegerField()
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

