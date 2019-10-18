import os
import time
from datetime import datetime

import paramiko
from uuid import uuid1
from django.core.paginator import Paginator
from fdfs_client.client import Fdfs_client
from rest_framework.response import Response
from rest_framework.views import APIView
from fdfs_client.client import Fdfs_client

# Create your views here.
from admin01.serializer import *
# 用户等级管理
from education import settings


def delete_file(url):
    name = url.split('M00')
    command = 'rm -rf /var/fdfs/storage/data/' + name[-1]
    # 实例化SSHClient
    client = paramiko.SSHClient()
    # 自动添加策略，保存服务器的主机名和密钥信息
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接SSH服务端，以用户名和密码进行认证
    client.connect(settings.IP, username=settings.USER, password=settings.PASSWORD)
    # 打开一个Channel并执行命令
    stdin, stdout, stderr = client.exec_command(command)
    # 打印执行结果
    print(stdout.readlines())
    # 关闭SSHClient
    client.close()


def get_pic_url(pic):
    # 获取图片路径的逻辑
    file = pic

    # print(pic)
    client = Fdfs_client("C:/fdfs.conf")
    # return ret
    if type(file) is not type(''):
        buffimg = b''  # 创建空的二进制流
        for chunk in file.chunks():
            buffimg += chunk  # 将图片传进流中
        return settings.PIC_URL + client.upload_by_buffer(buffimg, file_ext_name='jpg')['Remote file_id']
    else:
        return file


# 获取视频地址
class Video(APIView):
    def post(self, request):
        data = request.data
        video = get_pic_url(data['file'])
        print(data)
        mes = {}
        mes['url'] = video
        return Response(mes)


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
            paginator = Paginator(conditions, 10)
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
            t = Path.objects.get(id=data['id'])
            try:
                delete_file(t.pic)
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
            c1 = Path.objects.get(id=request.data['id'])
            data = request.data.copy()
            if data['pic'] == type(''):
                pass
            else:
                delete_file(c1.pic)
                data['pic'] = get_pic_url(data['pic'])
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
        dataList = LightPathSerializersModel(dataList, many=True)
        ret['dataList'] = dataList.data
        limit = request.GET.get('limit')
        if limit:
            ret['dataList'] = dataList.data[:int(limit)]
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)


# 阶段的增删改查
class PathStageView(APIView):
    # 展示
    def get(self, request):
        ret = {}
        try:
            id = request.GET.get('id')
            if id:
                tags = PathStage.objects.filter(path_id=int(id)).order_by('sort')
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
            id = request.data['id']
            t = Course.objects.get(id=id)
            try:
                delete_file(t.pic)
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
            c1 = Course.objects.get(id=request.data['id'])
            if data['pic'] == type(''):
                pass
            else:
                delete_file(c1.pic)
                data['pic'] = get_pic_url(data['pic'])
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

        limit = request.GET.get('limit')
        id = request.GET.get('id')
        if id:
            c = Course.objects.get(id=id)
            c = CourseSerializersModel(c, many=False)
            ret['dataList'] = c.data
            print(ret)
        elif limit:
            dataList = Course.objects.all()
            dataList = CourseSerializersModel(dataList, many=True)
            ret['dataList'] = dataList.data[:int(limit)]
        else:
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
        print(data)
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
                delete_file(t.pic)
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
        c1 = Teacher.objects.get(id=data['id'])
        if data['pic'] == type(''):
            pass
        else:
            delete_file(c1.pic)
            data['pic'] = get_pic_url(data['pic'])
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
        id = request.GET.get('id')
        if id:
            tea = Teacher.objects.filter(id=id).first()
            u = TeacherSerializersModel(tea, many=False)
        else:
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
            cid = request.GET.get('course_id')
            if cid:
                section = Section.objects.filter(course_id=cid).order_by('sort')
            elif id:
                section = Section.objects.get(id=id)
            else:
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
        c1 = Section.objects.get(id=data['id'])
        if c1.video == data['video']:
            pass
        else:
            delete_file(c1.pic)
            data['video'] = get_pic_url(data['video'])
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
                delete_file(t.pic)
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
        user_id = request.GET.get('user_id')
        if user_id:
            priceList = Price.objects.filter(course_id=course_id, user_id=user_id)
        else:
            priceList = Price.objects.filter(course_id=course_id)
        priceList = PriceSerializersModel(priceList, many=True)
        ret['dataList'] = priceList.data
        print(ret)
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


# http://116.62.155.103:8888/group1\M00/00/00/rBAdwl2eAzeAOA4TAAEsxfGKC08842.jpg
# http://116.62.155.103:8888/group1\M00/00/00/rBAdwl2eAmCAVME3AARjErJ7pcc779.jpg


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


class RuleAPIView(APIView):
    def get(self, request):
        ret = {}
        rule = Rule.objects.first()
        ret['rule'] = rule.ratio
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)


from datetime import datetime, timedelta


class SKAPIView(APIView):
    def get(self, request):
        ret = {}
        activeList = Act.objects.all()
        skList = Sk.objects.all()
        timeList = Time.objects.all()
        activeList = ActiveSerializersModel(activeList, many=True)
        skList = SkSerializersModel(skList, many=True)
        timeList = TimeSerializersModel(timeList, many=True)
        ret['activeList'] = activeList.data
        ret['skList'] = skList.data
        ret['timeList'] = timeList.data
        ret['code'] = 200
        ret['message'] = '成功'
        return Response(ret)

    def post(self, request):
        ret = {}
        ret['code'] = 200
        ret['message'] = '成功'
        data = request.data.copy()
        if data.get('start') and data.get('end'):
            data['start'] = datetime.strptime(data['start'].replace('T', ' ')[:-5], "%Y-%m-%d %H:%M:%S")+ timedelta(hours=8)
            data['end'] = datetime.strptime(data['end'].replace('T', ' ')[:-5], "%Y-%m-%d %H:%M:%S")+ timedelta(hours=8)
            print('添加时间')
            Time.objects.create(**data)
        elif data.get('title') and data.get('date'):
            print('添加活动')
            data['date'] = datetime.strptime(data['date'].replace('T', ' ')[:-5], "%Y-%m-%d %H:%M:%S")+ timedelta(hours=8)
            data['date']=data['date']
            print(data)
            Act.objects.create(**data)
        elif data.get('course_id') and data.get('time_id') and data.get('act_id'):
            print('添加秒杀商品')
            Sk.objects.create(course_id=data.get('course_id'), time_id=data['time_id'], act_id=data['act_id'],
                              sk_price=data['sk_price'], count=data['count'])
        else:
            ret['code'] = 601
            ret['message'] = '失败'
        return Response(ret)

    def delete(self, request):
        data = request.data.copy()
        mes = {}
        mes['code'] = 200
        mes['msg'] = "删除成功"
        if data.get('sk_id'):
            Sk.objects.get(id=data.get('sk_id')).delete()
        elif data.get('time_id'):
            Time.objects.get(id=data.get('time_id')).delete()
        elif data.get('active_id'):
            Act.objects.get(id=data.get('active_id')).delete()
        else:
            mes['code'] = 400
            mes['msg'] = "删除失败"
        return Response(mes)
