from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
import django.utils.timezone as timezone


# # Create your models here.
class Base(models.Model):
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)

    class Meta():
        abstract = True  # 这个类不生成对象


class UserLevel(models.Model):
    level = models.CharField(max_length=50)  # 用户等级

    class Meta():
        db_table = 'userlevel'


class User(Base, AbstractUser):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    img = models.CharField(max_length=255, default='')  # 用户头像
    username = models.CharField(max_length=50, unique=True)
    level = models.ForeignKey(UserLevel, on_delete=models.SET_NULL, blank=True, null=True)  # 用户等级
    integral = models.IntegerField(default=0)  # 积分
    invitation_code = models.CharField(max_length=100)  # 邀请码

    class Meta():
        db_table = 'user'


# 维护会员状态
class Member(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(UserLevel, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now())  # 会员生效时间
    end_time = models.DateTimeField(default=timezone.now())  # 会员失效时间

    class Meta():
        db_table = 'member'


class MemberOrder(Base):
    order_sn = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(UserLevel, on_delete=models.CASCADE)  # 开通的会员类型
    time = models.IntegerField(default=1)  # 开通时长
    code = models.CharField(max_length=100)  # 流水号
    status = models.IntegerField(default=0)  # 支付状态
    amount = models.DecimalField(max_digits=7, decimal_places=2)  # 总价
    pay_type = models.IntegerField()  # 支付方式
    invitation_code = models.CharField(max_length=100, default='')  # 使用的邀请码

    class Meta():
        db_table = 'memberorder'


class UserLevelCondition(models.Model):
    level = models.ForeignKey(UserLevel, on_delete=models.CASCADE)  # 开通的会员类型
    time = models.IntegerField(default=1)  # 开通时长
    amount = models.DecimalField(max_digits=7, decimal_places=2)  # 总价

    class Meta():
        db_table = 'userlevelcondition'


# 三方账号表
class ThirdPartyLogin(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField()  # 三方平台类型
    uid = models.CharField(max_length=50)  # 三方平台账号唯一的UID

    class Meta():
        db_table = 'thirdpartylogin'


# 站内信
class SiteMessage(Base):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta():
        db_table = 'sitemessage'


# 我的站内信
class UserSiteMessage(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    message = models.ForeignKey(SiteMessage, on_delete=models.CASCADE)

    class Meta():
        db_table = 'usersitemessage'


# 路径表
class Path(models.Model):
    name = models.CharField(max_length=50)
    pic = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    study_num = models.IntegerField()

    class Meta():
        db_table = 'path'


class UserPath(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.ForeignKey(Path, on_delete=models.CASCADE)

    class Meta():
        db_table = 'userpath'


class PathStage(models.Model):
    name = models.CharField(max_length=50, default='')
    path = models.ForeignKey(Path, on_delete=models.CASCADE)
    sort = models.IntegerField()

    class Meta():
        db_table = 'pathstage'


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)
    pic = models.CharField(max_length=255)

    class Meta():
        db_table = 'teacher'


class UserTeacher(models.Model):  # 用户关注表
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta():
        db_table = 'userteacher'


# 角色表
class Roles(Base):
    name = models.CharField(max_length=49, verbose_name='名称')
    status = models.IntegerField(default=0, verbose_name='是否启用')

    class Meta():
        db_table = 'roles'


# 资源表
class Resources(Base):
    name = models.CharField(max_length=40, verbose_name='资源名')
    url = models.CharField(max_length=100, verbose_name='资源地址')
    status = models.IntegerField(default=1, verbose_name='状态0停用1启用')

    class Meta():
        db_table = 'resources'


# 角色资源表
class RoleResource(Base):
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name='角色id')
    resources = models.ForeignKey(Resources, on_delete=models.CASCADE, verbose_name='资源id')

    class Meta():
        db_table = 'roleresource'


# 管理员用户表
class Admin(Base):
    username = models.CharField(max_length=100, verbose_name='管理用户名')
    password = models.CharField(max_length=200, verbose_name='管理用户密码')
    roles = models.ForeignKey('Roles', on_delete=models.CASCADE, verbose_name='外键角色id')

    # is_admin = models.IntegerField()
    class Meta():
        db_table = 'admin'


# 秒杀时间表
class Time(Base):
    start = models.TimeField()
    end = models.TimeField()

    class Meta():
        db_table = 'time'


# 活动表
class Act(Base):
    title = models.CharField(max_length=40, default='', verbose_name='标题')
    date = models.DateField(verbose_name='活动时间定为到天')

    class Meta():
        db_table = 'act'


class Sk(Base):
    act = models.ForeignKey(Act, on_delete=models.CASCADE, verbose_name='对应活动表')
    time = models.ForeignKey('Time', on_delete=models.CASCADE, verbose_name='对应时间表')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='对应课程表')
    sk_price = models.DecimalField(max_digits=7, decimal_places=2, default=999.00)
    count = models.IntegerField(default=0)

    class Meta():
        db_table = 'sk'


# 课程标签表
class Tag(Base):
    name = models.CharField(max_length=50, verbose_name='标签名称')

    class Meta():
        db_table = 'tag'


# 课程表
class Course(Base):
    title = models.CharField(max_length=50, verbose_name='课程标题')
    pic = models.CharField(max_length=255, verbose_name='课程图片')
    info = models.CharField(max_length=255, verbose_name='课程简介')
    # 是否上线 0没上线 1上线
    online = models.IntegerField(default=1, verbose_name='是否上线')
    # 是否会员 0非会员 1会员2训练营
    member = models.IntegerField(default=1, verbose_name='是否会员')
    attention = models.IntegerField(verbose_name='关注量')
    learn = models.IntegerField(verbose_name='学过人数')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='老师外键')
    comment_num = models.IntegerField(verbose_name='评论数')
    pathstage = models.ForeignKey(PathStage, on_delete=models.CASCADE, verbose_name='阶段外键', null=True)
    path = models.ForeignKey(Path, on_delete=models.CASCADE, verbose_name='路径', null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='标签外键')
    recommand = models.CharField(max_length=50, verbose_name='推荐课程')
    detail = models.CharField(max_length=255, verbose_name='课程详情')
    section_num = models.IntegerField(verbose_name='章节数')

    class Meta():
        db_table = 'course'


# 课程章节表
class Section(Base):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.CharField(max_length=50, verbose_name='课程章节名称')
    video = models.CharField(max_length=255, verbose_name='视频连接')
    sort = models.IntegerField(verbose_name='排序')

    class Meta():
        db_table = 'section'


# 学习记录表
class UserCourse(Base):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程外键')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='章节外键')
    # 完成状态0未完成1完成
    status = models.IntegerField(default=1)

    class Meta():
        db_table = 'user_course'


# 课程收藏表
class CourseCollect(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta():
        db_table = 'course_collect'


# 价格表
class Price(Base):
    # 类型（普通/会员/高级会员）
    type = models.IntegerField(default=1, verbose_name='类型')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程ID')
    discount = models.FloatField(verbose_name='折扣')
    discoun_price = models.DecimalField(verbose_name='折扣后', max_digits=7, decimal_places=2)

    class Meta():
        db_table = 'price'


#
# 实验报告表
class Report(Base):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='章节ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户ID')
    report_content = models.TextField(max_length=2000, default='')
    report_title = models.CharField(max_length=50, verbose_name='报告标题')
    report_browse = models.IntegerField(verbose_name='实验报告浏览量', default=0)
    linknum = models.IntegerField(verbose_name='点赞树', default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程ID')

    class Meta():
        db_table = 'report'


# 用户和收藏实验问答报告表
class Collect(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    find_id = models.IntegerField(verbose_name='实验问答id/实验ID')
    # 收藏类型（0实验报告/1实验问答）
    collect_type = models.IntegerField(default=1)

    class Meta():
        db_table = 'collect'


# 订单记录表
class OrderRecord(Base):
    order_number = models.CharField(max_length=100)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='关联用户id')
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='关联课程id')
    pay_type = models.IntegerField(default=0, verbose_name='支付方式01')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='支付价格')
    pay_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='价实际格')
    preferential_way = models.IntegerField(default=0, verbose_name='优惠方式，0未使用优惠，1使用积分，2使用优惠券')
    preferential_money = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='优惠金额')
    use_type = models.IntegerField(default=0, verbose_name='是否使用优惠券')
    order_status = models.IntegerField(default=0, verbose_name='订单状态')
    code = models.CharField(max_length=100, verbose_name='流水号')
    coupon = models.CharField(max_length=100, verbose_name='如果使用优惠券则填优惠券的码，不使用则为空')
    pay_status = models.IntegerField(default=0, verbose_name='支付状态')
    num = models.IntegerField(default=0, verbose_name='消耗积分')

    class Meta():
        db_table = 'orderrecord'


# 积分兑换规则
class Rule(Base):
    ratio = models.IntegerField()  # 积分抵现比例
    invite_award = models.IntegerField(default=10)  # 邀请奖励
    learn_award = models.IntegerField(default=10)  # 课程学习奖励

    class Meta:
        db_table = 'rule'


# 优惠券表
class Coupon(Base):
    name = models.CharField(max_length=15, verbose_name='优惠券名称')
    count = models.IntegerField(verbose_name='优惠券数量')
    type = models.IntegerField(verbose_name='优惠券类型')  # 1首次注册会员送  2全场能用  3指定商品  4指定会员
    course = models.IntegerField(verbose_name='类型为3时指定课程')
    start_time = models.DateTimeField(verbose_name='会员开始时间', default=timezone.now())
    end_time = models.DateTimeField(verbose_name='会员结束时间', default=timezone.now())
    status = models.IntegerField(verbose_name='使用状态')  # 1可用，2不可用
    condition = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='满多少钱可以使用')
    money = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='优惠券金额')
    value = models.IntegerField(default=0)  # 换优惠券需要多少积分

    class Meta:
        db_table = 'coupon'


# 用户优惠券表
class Usercoupon(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, verbose_name='优惠券名称', default='')
    type = models.IntegerField(verbose_name='优惠券类型', default=0)  # 1首次注册会员送  2全场能用  3指定商品  4指定会员
    code = models.CharField(verbose_name='优惠券唯一编码', default='', max_length=255)
    start_time = models.DateTimeField(verbose_name='优惠券开始时间', default=timezone.now())
    end_time = models.DateTimeField(verbose_name='优惠券结束时间', default=timezone.now())
    money = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='优惠券金额')
    condition = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='满多少钱可以使用')
    is_use = models.IntegerField(verbose_name='是否使用')  # 0未使用，1使用
    cid = models.IntegerField(default=0)
    course_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'usercoupon'


# 积分记录表
class CreditsLog(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    x_integral = models.IntegerField(default=1)
    s_integral = models.IntegerField(verbose_name='变化前总积分')
    before_integral = models.IntegerField(verbose_name='本次操作积分')
    end_integral = models.IntegerField(verbose_name='积分兑换用途')
    effect = models.IntegerField(verbose_name='兑换的码')
    coupon_code = models.CharField(max_length=250)


# 焦点图
class Picture(Base):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=250)
    pic = models.CharField(max_length=250)
    type = models.IntegerField(default=1)


# 工单表
class WorkOrder(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    pid = models.IntegerField(default=0)
    status = models.IntegerField(default=0)


# 日志表
class Data(Base):
    dates = models.DateTimeField(auto_now_add=True, verbose_name='执行时间')
    operation = models.CharField(max_length=250)
    result = models.IntegerField(default=1)
    reason = models.CharField(max_length=250)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

#
# # 实验问答
# class Answer(Base):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程ID')
#     answer_content = models.CharField(max_length=50, verbose_name='问答标题')
#     answer_title = models.CharField(max_length=50, verbose_name='问答内容')
#     browse = models.IntegerField(verbose_name='浏览量')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     pid = models.IntegerField(verbose_name='上一级评论ID')
#     top = models.IntegerField(verbose_name='顶级评论ID')
#     type = models.IntegerField(verbose_name='自身级别ID')
#
#     class Meta():
#         db_table = 'answer'


#
# # 讨论区表
# class Forum(Base):
#     title = models.CharField(max_length=100, verbose_name='标题')
#     content = models.CharField(max_length=255, verbose_name='内容')
#     user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='关联用户')
#     top = models.IntegerField(default=0, verbose_name='顶级id')
#     revert_num = models.IntegerField(default=0, verbose_name='回复数')
#     look_num = models.IntegerField(default=0, verbose_name='查看数')
#     end_revert_num = models.IntegerField(default=0, verbose_name='最后回复的用户id')
#     type = models.IntegerField(default=0, verbose_name='类型（0交流讨论/1技术分享/2站内公告）')
#     status = models.IntegerField(default=0, verbose_name='审核状态')
#
#     class Meta():
#         db_table = 'forum'


#
#
# # #评论p
# # class Comment(Base):
# #     content = models.CharField(max_length=50,verbose_name='评论内容')
# #     pid = models.IntegerField(verbose_name='上一级评论ID')
# #     top = models.IntegerField(verbose_name='顶级评论ID')
# #     type =models.IntegerField(verbose_name='自身级别ID')
# #     user = models.IntegerField(verbose_name='用户ID')
# #     course = models.IntegerField(verbose_name='课程ID')
# #     comment_type = models.IntegerField(verbose_name='评论类型')
# #     # 审核状态（0否1是）
# #     status = models.IntegerField(default=1)
# #     reason = models.CharField(max_length=250,verbose_name='失败原因')
# #
# #     class Meta():
# #         db_table = 'comment'
