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
        m = SiteMessage.objects.create(**data)
        return m

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.save()
        return instance


# 路径系列化类

class PathSerializersModel(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = '__all__'


# 路径反序列化类
class PathSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    pic = serializers.CharField(max_length=255)
    info = serializers.CharField(max_length=255)
    study_num = serializers.IntegerField(default=0)

    def create(self, data):
        m = Path.objects.create(**data)
        return m

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.pic = validated_data['pic']
        instance.info = validated_data['info']
        instance.study_num = validated_data['study_num']
        instance.save()
        return instance


# 阶段的序列化
class PathStageSerializersModel(serializers.ModelSerializer):
    path_name = serializers.CharField(source='path.name')
    path_id = serializers.CharField()

    class Meta:
        model = PathStage
        fields = '__all__'


# 阶段的反序列化
class PathStageSerializers(serializers.Serializer):
    path_id = serializers.IntegerField()
    sort = serializers.IntegerField()

    def create(self, data):
        m = PathStage.objects.create(**data)
        return m

    def update(self, instance, validated_data):
        instance.path_id = validated_data['path_id']
        instance.sort = validated_data['sort']
        instance.save()
        return instance


# 课程序列化
class CourseSerializersModel(serializers.ModelSerializer):
    teacher = serializers.CharField(source='teacher.name')
    path = serializers.CharField(source='pathstage.name')
    tag = serializers.CharField(source='tag.name')
    teacher_id = serializers.IntegerField()
    path_id = serializers.IntegerField()
    tag_id = serializers.IntegerField()

    class Meta:
        model = Course
        fields = '__all__'


# 课程反序列化
class CourseSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    pic = serializers.CharField(max_length=255)
    info = serializers.CharField(max_length=255)
    teacher_id = serializers.IntegerField()
    path_id = serializers.IntegerField()
    online = serializers.IntegerField()
    member = serializers.IntegerField()
    attention = serializers.IntegerField()
    learn = serializers.IntegerField()
    comment_num = serializers.IntegerField()
    tag_id = serializers.IntegerField()
    section_num = serializers.IntegerField()
    recommand = serializers.CharField(max_length=50)
    detail = serializers.CharField(max_length=50)

    def create(self, data):
        m = Course.objects.create(**data)
        return m

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.pic = validated_data['pic']
        instance.info = validated_data['info']
        instance.teacher_id = validated_data['teacher_id']
        instance.path_id = validated_data['path_id']
        instance.online = validated_data['online']
        instance.member = validated_data['member']
        instance.attention = validated_data['attention']
        instance.learn = validated_data['learn']
        instance.comment_num = validated_data['comment_num']
        instance.tag_id = validated_data['tag_id']
        instance.section_num = validated_data['section_num']
        instance.recommand = validated_data['recommand']
        instance.detail = validated_data['detail']
        instance.save()
        return instance


# 讲师的序列化
class TeacherSerializersModel(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


# 讲师序列化
class TeacherSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    desc = serializers.CharField(max_length=255)
    pic = serializers.CharField(max_length=255)


    def create(self, data):
        m = Teacher.objects.create(**data)
        return m

    def update(self, instance, validated_data):
        instance.path_id = validated_data['path_id']
        instance.sort = validated_data['sort']
        instance.save()
        return instance
