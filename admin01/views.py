
import os
import paramiko
from uuid import uuid1
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from admin01.serializer import *
# 用户等级管理
from education import settings


class LevelAPIView(APIView):
    def post(self, request):  # 添加等级
        ret = {}
        try:
            data = request.data
            UserLevel.objects.create(level=data['level'])
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def delete(self, request):  # 删除等级
        ret = {}
        try:
            data = request.data
            UserLevel.objects.get(id=data['id']).delete()
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def put(self, request):  # 修改等级
        ret = {}
        try:
            data = request.data
            obj = UserLevel.objects.get(id=data['id'])
            obj.level = data['level']
            obj.save()
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def get(self, request):  # 展示标签
        ret = {}
        levels = UserLevel.objects.all()
        levels = UserLevelSerializer(levels, many=True)
        ret['levels'] = levels.data
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)


# 课程标签管理
class TagAPIView(APIView):
    def post(self, request):  # 添加标签
        ret = {}
        try:
            data = request.data
            print(data)
            Tag.objects.create(name=data['name'])
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def delete(self, request):  # 删除标签
        ret = {}
        try:
            data = request.data

            Tag.objects.get(id=data['id']).delete()
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def put(self, request):  # 修改标签
        ret = {}
        try:
            data = request.data
            obj = Tag.objects.get(id=data['id'])
            obj.name = data['name']
            obj.save()
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def get(self, request):  # 展示标签
        ret = {}
        try:
            tags = Tag.objects.all()
            tags = TagSerializersModel(tags, many=True)
            ret['tags'] = tags.data
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as ex:
            print(ex)
            ret['code'] = 601
            ret['message'] = '数据库错误'

        return Response(ret)


# 用户等级条件管理
class ConditionAPIView(APIView):
    def post(self, request):  # 添加用户等级条件 参数 id ,level_id ,amount, time
        mes = {}
        try:
            ser = UserLevelConditionSerializers(data=request.data)
            if ser.is_valid():
                ser.save()
                mes['code'] = 200
                mes['message'] = '成功'
                mes['data'] = ser.data
            else:
                print(ser.errors)
                mes['code'] = 601
                mes['message'] = '失败'
        except Exception as ex:
            print(ex)
            mes['code'] = 601
            mes['message'] = '数据库错误'
        return Response(mes)

    def delete(self, request):  # 删除条件
        ret = {}
        try:
            data = request.data
            UserLevelCondition.objects.get(id=data['id']).delete()
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def put(self, request):  # 修改条件 参数 id ,level_id ,amount, time
        mes = {}
        try:
            id = request.data['id']
            c1 = UserLevelCondition.objects.get(id=id)
            ser = UserLevelConditionSerializers(c1, data=request.data)
            if ser.is_valid():
                ser.save()
                mes['code'] = 200
                mes['message'] = '成功'
                mes['data'] = ser.data
            else:
                print(ser.errors)
                mes['code'] = 601
                mes['message'] = '失败'
        except Exception as es:
            mes['code'] = 601
            mes['message'] = '数据库错误'
        return Response(mes)

    def get(self, request):
        ret = {}
        try:
            p = request.GET.get('p')
            conditions = UserLevelCondition.objects.all()
            paginator = Paginator(conditions, 2)
            conditions = paginator.page(int(p))
            conditions = ConditionSerializersModel(conditions, many=True)
            ret['conditions'] = conditions.data
            ret['currentPage'] = p
            ret['totalPage'] = paginator.num_pages
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as ex:
            print(ex)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)


# 站内信管理
class SiteMessageAPIView(APIView):
    def post(self, request):  # 添加站内信
        ret = {}
        try:
            data = request.data
            ser = SiteMessageSerializers(data=data)
            if ser.is_valid():
                ser.save()
                ret['code'] = 200
                ret['message'] = '成功'
            else:
                print(ser.errors)
                ret['code'] = 601
                ret['message'] = '失败'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def delete(self, request):  # 删除站内信
        ret = {}
        try:
            data = request.data
            SiteMessage.objects.get(id=data['id']).delete()
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def put(self, request):  # 修改站内信
        ret = {}
        try:
            data = request.data
            c1 = SiteMessage.objects.get(id=request.data['id'])
            ser = SiteMessageSerializers(c1, data=data)
            if ser.is_valid():
                ser.save()
                ret['code'] = 200
                ret['message'] = '成功'
            else:
                print(ser.errors)
                ret['code'] = 601
                ret['message'] = '失败'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def get(self, request):  # 展示站内信
        ret = {}
        dataList = SiteMessage.objects.all()
        dataList = SiteMessageSerializersModel(dataList, many=True)
        ret['levels'] = dataList.data
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)


# 路径管理
class PathAPIView(APIView):
    def post(self, request):  # 添加路径
        ret = {}
        try:
            data = request.data.copy()
            # 图片上传逻辑
            print(data, '==============')
            data['pic'] = get_pic_url(data['pic'])
            ser = PathSerializers(data=data)
            if ser.is_valid():
                ser.save()
                ret['code'] = 200
                ret['message'] = '成功'
            else:
                print(ser.errors)
                ret['code'] = 601
                ret['message'] = '失败'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def delete(self, request):  # 删除路径
        ret = {}
        try:
            data = request.data
            t = Path.objects.get(id=id)
            try:
                os.remove(os.path.join(settings.STATICFILES_DIRS[0], t.pic.split("/")[-1]))
            except:
                pass
            t.delete()
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def put(self, request):  # 修改路径
        ret = {}
        try:
            data = request.data.copy()
            data['pic'] = get_pic_url(data['pic'])
            c1 = Path.objects.get(id=request.data['id'])
            ser = PathSerializers(c1, data=data)
            if ser.is_valid():
                ser.save()
                ret['code'] = 200
                ret['message'] = '成功'
            else:
                print(ser.errors)
                ret['code'] = 601
                ret['message'] = '失败'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def get(self, request):  # 展示路径
        ret = {}
        dataList = Path.objects.all()
        dataList = PathSerializersModel(dataList, many=True)
        ret['dataList'] = dataList.data
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)


def get_pic_url(pic):
    # 获取图片路径的逻辑
    file = pic

    # print(pic)
    # client = Fdfs_client("client.conf")
    # ret=client.upload_by_buffer(pic)
    # # ret = client.upload_by_filename('1.jpg')
    # print(ret,'========================')
    # return ret
    if type(file) is not type(''):
        name = str(uuid1()) + file.name
        # f = open(os.path.join(settings.UPLOAD_ROOT,'',file.name),'wb')
        f = open(os.path.join(settings.STATICFILES_DIRS[0], name), 'wb')
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        return settings.PIC_URL + name
    else:
        return file


# 阶段的增删改查
class PathStageView(APIView):
    # 展示
    def get(self, request):
        ret = {}
        try:
            id = request.GET.get('id')
            if id:
                tags = PathStage.objects.filter(path_id=int(id)).all()
            else:
                tags = PathStage.objects.all()
            tags = PathStageSerializersModel(tags, many=True)
            ret['tags'] = tags.data
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as ex:
            print(ex)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    # 增加
    def post(self, request):
        mes = {}
        try:
            ser = PathStageSerializers(data=request.data)
            if ser.is_valid():
                ser.save()
                mes['code'] = 200
                mes['message'] = '成功'
                mes['data'] = ser.data
            else:
                print(ser.errors)
                mes['code'] = 601
                mes['message'] = '失败'
        except Exception as ex:
            print(ex)
            mes['code'] = 601
            mes['message'] = '数据库错误'
        return Response(mes)
        # 修改

    def put(self, request):
        mes = {}
        try:
            id = request.data['id']
            c1 = PathStage.objects.get(id=id)
            ser = PathStageSerializers(c1, data=request.data)
            if ser.is_valid():
                ser.save()
                mes['code'] = 200
                mes['message'] = '成功'
                mes['data'] = ser.data
            else:
                print(ser.errors)
                mes['code'] = 601
                mes['message'] = '失败'
        except Exception as es:
            mes['code'] = 601
            mes['message'] = '数据库错误'
        return Response(mes)

    # 删除
    def delete(self, request):
        mes = {}
        try:
            data = request.data
            PathStage.objects.get(id=data['id']).delete()
            mes['code'] = 200
            mes['message'] = '成功'
        except Exception as es:
            print(es)
            mes['code'] = 601
            mes['message'] = '数据库错误'
        return Response(mes)


# 课程管理
class CourseAPIView(APIView):
    def post(self, request):  # 添加 课程
        ret = {}
        try:
            data = request.data.copy()
            print(data)
            # 图片上传逻辑
            data['pic'] = get_pic_url(data['pic'])
            ser = CourseSerializers(data=data)
            if ser.is_valid():
                ser.save()
                ret['code'] = 200
                ret['message'] = '成功'
            else:
                print(ser.errors)
                ret['code'] = 601
                ret['message'] = '失败'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def delete(self, request):  # 删除课程
        ret = {}
        try:
            data = request.data
            t = Course.objects.get(id=id)
            try:
                os.remove(os.path.join(settings.STATICFILES_DIRS[0], t.pic.split("/")[-1]))
            except:
                pass
            t.delete()
            ret['code'] = 200
            ret['message'] = '成功'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def put(self, request):  # 修改课程
        ret = {}
        try:
            data = request.data.copy()
            data['pic'] = get_pic_url(data['pic'])
            c1 = Course.objects.get(id=request.data['id'])
            ser = CourseSerializers(c1, data=data)
            if ser.is_valid():
                ser.save()
                ret['code'] = 200
                ret['message'] = '成功'
            else:
                print(ser.errors)
                ret['code'] = 601
                ret['message'] = '失败'
        except Exception as es:
            print(es)
            ret['code'] = 601
            ret['message'] = '数据库错误'
        return Response(ret)

    def get(self, request):  # 展示课程
        ret = {}
        dataList = Course.objects.all()
        dataList = CourseSerializersModel(dataList, many=True)
        ret['dataList'] = dataList.data
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)


# 讲师管理
class TeacherAPIView(APIView):
    def post(self, request):
        data = request.data.copy()
        print(data)
        data['pic'] = get_pic_url(data['pic'])
        ser = TeacherSerializers(data=data)
        mes = {}
        if ser.is_valid():
            ser.save()
            mes['code'] = 200
            mes['msg'] = 'ok'

        else:
            print(ser.errors)
            mes['code'] = 400
            mes['msg'] = '失败'
        return Response(mes)

    def delete(self, request):
        id = request.data['id']

        mes = {}
        if id:
            t = Teacher.objects.get(id=id)
            try:
                os.remove(os.path.join(settings.STATICFILES_DIRS[0], t.pic.split("/")[-1]))
            except:
                pass
            t.delete()
            mes['code'] = 200
            mes['msg'] = "删除成功"
        else:
            mes['code'] = 400
            mes['msg'] = "删除失败"
        return Response(mes)

    def put(self, request):
        data = request.data.copy()
        print(data)
        data['pic'] = get_pic_url(data['pic'])
        c1 = Teacher.objects.get(id=data['id'])
        ser = TeacherSerializers(c1, data=data)
        mes = {}
        if ser.is_valid():
            ser.save()
            mes['code'] = 200
            mes['msg'] = 'ok'

        else:
            print(ser.errors)
            mes['code'] = 400
            mes['msg'] = '失败'
        return Response(mes)

    def get(self, request):
        tea = Teacher.objects.all()
        u = TeacherSerializersModel(tea, many=True)
        mes = {}
        mes['code'] = 200
        mes['dataList'] = u.data
        return Response(mes)


# 章节列表
class SectionView(APIView):
    def get(self, request):
        mes = {}
        try:
            section = Section.objects.all()
            s = SectionSerializersModel(section, many=True)
            mes['code'] = 200
            mes['message'] = 'ok'
            mes['dataList'] = s.data
        except:
            mes['code'] = 10010
            mes['message'] = '数据库请求失败'
        return Response(mes)

    def post(self, request):
        mes = {}
        data = request.data
        # data['video'] = get_pic_url(data['video'])
        if data:
            s = SectionSerializers(data=data)
            if s.is_valid():
                s.save()
                mes['code'] = 200
                mes['message'] = 'ok'
            else:
                print(s.errors)
                mes['code'] = 10020
                mes['message'] = '添加失败'
        else:
            mes['code'] = 10030
            mes['message'] = '获取数据不全'
        return Response(mes)

    def put(self, request):
        data = request.data.copy()
        data['video'] = get_pic_url(data['video'])
        print(data)
        c1 = Section.objects.get(id=data['id'])
        ser = SectionSerializers(c1, data=data)
        mes = {}
        if ser.is_valid():
            ser.save()
            mes['code'] = 200
            mes['msg'] = 'ok'
        else:
            print(ser.errors)
            mes['code'] = 400
            mes['msg'] = '失败'
        return Response(mes)

    def delete(self, request):
        id = request.data['id']
        mes = {}
        if id:
            t = Section.objects.get(id=id)
            try:
                os.remove(os.path.join(settings.STATICFILES_DIRS[0], t.pic.split("/")[-1]))
            except:
                pass
            t.delete()
            mes['code'] = 200
            mes['msg'] = "删除成功"
        else:
            mes['code'] = 400
            mes['msg'] = "删除失败"
        return Response(mes)


# 价格
class SetPriceAPIView(APIView):
    def get(self, request):  # 展示价格
        ret = {}
        course_id = request.GET.get('course_id')
        priceList = Price.objects.filter(course_id=course_id)
        priceList = PriceSerializersModel(priceList, many=True)
        ret['dataList'] = priceList.data
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)

    # 添加价格
    def post(self, request):
        ret = {}
        data = request.data
        print(data['levels'])
        for level in data['levels']:
            # 一次性将所有会员对应的价格添加
            ser = PriceSerializers(data={'type': level['id'],  # 会员id
                                         'course_id': data['course_id'],  # 课程id
                                         'discount': level['discount'],  # 打几折
                                         'discoun_price': float(data['price']) * float(level['discount'], ) * 0.1
                                         # 折后价格
                                         })
            if ser.is_valid():
                ser.save()
        print(data)
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)

    def put(self, request):
        # 修改偷懒了,将旧价格删掉,重新填新价格
        ret = {}
        data = request.data
        print(data)
        p = Price.objects.filter(course_id=data['course_id']).all()
        for level in data['levels']:
            p = Price.objects.filter(course_id=data['course_id'], type=level['id']).first()
            ser = PriceSerializers(p, data={'type': level['id'],
                                            'course_id': data['course_id'],
                                            'discount': level['discount'],
                                            'discoun_price': float(data['price']) * float(level['discount'], ) * 0.1
                                            })
            if ser.is_valid():
                ser.save()
        print(data)
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)


# 获取视频地址
class Video(APIView):
    def post(self, request):
        data = request.data
        video = get_pic_url(data['file'])
        print(data)
        mes = {}
        mes['url'] = video
        return Response(mes)


# 备份数据库
class BackupsAPIView(APIView):
    def get(self, request):
        ret = {}
        # 实例化SSHClient
        client = paramiko.SSHClient()
        # 自动添加策略，保存服务器的主机名和密钥信息
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接SSH服务端，以用户名和密码进行认证
        client.connect(settings.IP, username=settings.USER, password=settings.PASSWORD)
        # 打开一个Channel并执行命令
        command = 'sh /home/backupdb.sh'
        stdin, stdout, stderr = client.exec_command(command)
        # 打印执行结果
        print(stdout.readlines())
        # 关闭SSHClient
        client.close()
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)


# 优惠券的增删改查
class CouponView(APIView):
    def get(self, request):
        coupon = Coupon.objects.all()
        ser = CouponModelSerializer(instance=coupon, many=True)
        mes = {}
        mes['code'] = 200
        mes['message'] = '查询成功'
        mes['dataList'] = ser.data
        return Response(mes)

    def post(self, request):
        mes = {}
        data = request.data
        print(type(data['start_time']))
        print(data)
        # data['video'] = get_pic_url(data['video'])
        if data:
            s = CouponSerializer(data=data)
            if s.is_valid():
                s.save()
                mes['code'] = 200
                mes['message'] = 'ok'
            else:
                print(s.errors)
                mes['code'] = 10020
                mes['message'] = '添加失败'
        else:
            mes['code'] = 10030
            mes['message'] = '获取数据不全'
        return Response(mes)

    def put(self, request):
        data = request.data.copy()
        c1 = Coupon.objects.get(id=data['id'])
        ser = CouponSerializer(c1, data=data)
        mes = {}
        if ser.is_valid():
            ser.save()
            mes['code'] = 200
            mes['msg'] = 'ok'
        else:
            print(ser.errors)
            mes['code'] = 400
            mes['msg'] = '失败'
        return Response(mes)

    def delete(self, request):
        id = request.data['id']
        mes = {}
        if id:
            Coupon.objects.get(id=id).delete()
            mes['code'] = 200
            mes['msg'] = "删除成功"
        else:
            mes['code'] = 400
            mes['msg'] = "删除失败"
        return Response(mes)



