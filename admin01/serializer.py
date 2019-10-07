from rest_framework import serializers
from admin01.models import *


# 用户等级序列化类
class UserLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLevel
        fields = "__all__"


# 用户等级条件序列化类
class ConditionSerializersModel(serializers.ModelSerializer):
    level = serializers.CharField(source='level.level')
    level_id = serializers.IntegerField()

    class Meta:
        model = UserLevelCondition
        fields = '__all__'


# 用户等级条件反序列化类
class UserLevelConditionSerializers(serializers.Serializer):
    level_id = serializers.IntegerField()
    time = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=7, decimal_places=2)

    def create(self, data):
        m = UserLevelCondition.objects.create(**data)
        return m

    def update(self, instance, validated_data):
        instance.level_id = validated_data['level_id']
        instance.time = validated_data['time']
        instance.amount = validated_data['amount']
        instance.save()
        return instance


# 标签的序列化类
class TagSerializersModel(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# 站内信的序列化类
class SiteMessageSerializersModel(serializers.ModelSerializer):
    class Meta:
        model = SiteMessage
        fields = '__all__'


# 站内信的反系列化类
class SiteMessageSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    content = serializers.CharField()

    def create(self, data):
        m = UserLevelCondition.objects.create(**data)
        return m

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.save()
        return instance
