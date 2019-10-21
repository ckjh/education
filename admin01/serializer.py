from rest_framework import serializers
from admin01.models import *


# 用户等级序列化类
class UserLevelSerializer(serializers.ModelSerializer):
    discount = serializers.DecimalField(max_digits=7, decimal_places=2, default=10)

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


# 路径序列化类

class PathSerializersModel(serializers.ModelSerializer):
    num = serializers.SerializerMethodField()
    stageList = serializers.SerializerMethodField()

    def get_num(self, row):
        try:
            n = Course.objects.filter(path_id=row.id).count()
        except:
            n = 0
        return n

    def get_stageList(self, row):
        try:
            sList = PathStage.objects.filter(path_id=row.id).order_by('sort')
            sList = PathStageSerializersModel(sList, many=True)
            return sList.data
        except:
            return []

    class Meta:
        model = Path
        fields = '__all__'


class LightPathSerializersModel(serializers.ModelSerializer):
    num = serializers.SerializerMethodField()

    def get_num(self, row):
        try:
            n = Course.objects.filter(path_id=row.id).count()
        except:
            n = 0
        return n

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
    courseList = serializers.SerializerMethodField()

    def get_courseList(self, row):
        try:
            cList = Course.objects.filter(pathstage_id=row.id).all()
            cList = CourseSerializersModel(cList, many=True)
            return cList.data
        except:
            return []

    class Meta:
        model = PathStage
        fields = '__all__'


# 阶段的反序列化
class PathStageSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
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
    pathstage = serializers.CharField(source='pathstage.name')
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
    pathstage_id = serializers.IntegerField()
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
        instance.pathstage_id = validated_data['pathstage_id']
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
        instance.name = validated_data['name']
        instance.desc = validated_data['desc']
        instance.pic = validated_data['pic']
        instance.save()
        return instance


# 章节序列化
class SectionSerializersModel(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


# 章节反序列化
class SectionSerializers(serializers.Serializer):
    course_id = serializers.IntegerField()
    section = serializers.CharField()
    video = serializers.CharField()
    sort = serializers.IntegerField()

    def create(self, data):
        m = Section.objects.create(**data)
        return m

    def update(self, instance, validated_data):
        instance.course_id = validated_data['course_id']
        instance.section = validated_data['section']
        instance.video = validated_data['video']
        instance.sort = validated_data['sort']
        instance.save()
        return instance


# 价格的序列化类
class PriceSerializersModel(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()

    def get_level(self, row):
        if row.type > 0:
            c = UserLevel.objects.get(id=row.type)
            name = c.level
        else:
            name = ''
        return name

    class Meta:
        model = Price
        fields = '__all__'


class PriceSerializers(serializers.Serializer):
    type = serializers.IntegerField()
    course_id = serializers.IntegerField()
    discount = serializers.FloatField()
    discoun_price = serializers.DecimalField(max_digits=7, decimal_places=2)

    def create(self, data):
        m = Price.objects.create(**data)
        return m

    def update(self, instance, validated_data):
        instance.discount = validated_data['discount']
        instance.discoun_price = validated_data['discoun_price']
        instance.save()
        return instance


# 优惠券序列化
class CouponModelSerializer(serializers.ModelSerializer):
    # course = serializers.SlugRelatedField(slug_field='name',read_only=True)
    course_name = serializers.SerializerMethodField()

    def get_course_name(self, row):
        if row.course > 0:
            name = ''
            try:
                c = Course.objects.get(id=row.course)
                name = c.title
            except:
                name: ''
        else:
            name = ''
        return name

    class Meta:
        model = Coupon
        fields = '__all__'


class CouponSerializer(serializers.Serializer):
    name = serializers.CharField()  # 优惠券名称
    count = serializers.IntegerField()  # 优惠券数量
    type = serializers.IntegerField()  # 1首次注册会员送  2全场能用  3指定商品  4指定会员  #优惠券类型
    course = serializers.IntegerField(default=0)  # 类型为3时指定课程
    start_time = serializers.DateTimeField()  # 会员开始时间
    end_time = serializers.DateTimeField()  # 会员结束时间
    status = serializers.IntegerField()  # 1可用，2过期  #使用状态
    condition = serializers.DecimalField(max_digits=7, decimal_places=2)  # 满多少钱可以使用
    money = serializers.DecimalField(max_digits=7, decimal_places=2)  # 优惠券金额

    def create(self, data):
        m = Coupon.objects.create(**data)
        return m

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.count = validated_data['count']
        instance.type = validated_data['type']
        instance.course = validated_data['course']
        instance.start_time = validated_data['start_time']
        instance.end_time = validated_data['end_time']
        instance.status = validated_data['status']
        instance.condition = validated_data['condition']
        instance.money = validated_data['money']
        instance.save()
        return instance


class ActiveSerializersModel(serializers.ModelSerializer):
    class Meta:
        model = Act
        fields = '__all__'


class TimeSerializersModel(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'


class SkSerializersModel(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.title')
    act_name = serializers.CharField(source='act.title')
    start = serializers.CharField(source='time.start')
    end = serializers.CharField(source='time.end')
    pic = serializers.CharField(source='course.pic')
    info = serializers.CharField(source='course.info')
    section_num = serializers.CharField(source='course.section_num')
    date = serializers.CharField(source='act.date')

    class Meta:
        model = Sk
        fields = '__all__'


class UserSiteMessageSerializersModel(serializers.ModelSerializer):
    title = serializers.CharField(source='message.title')
    content = serializers.CharField(source='message.content')

    class Meta:
        model = UserSiteMessage
        fields = '__all__'


class UserCourseSerializersModel(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.title')
    pic = serializers.CharField(source='course.pic')
    section_name = serializers.CharField(source='section.section')

    class Meta:
        model = UserCourse
        fields = '__all__'
