"""education URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reception import views
from reception import pay

app_name = 'reception'
urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),  # 登录
    path('reg/', views.RegAPIView.as_view()),  # 注册
    path('getimagecode/', views.GetImageCode),  # 获取验证码图片
    path('forgetpwd/', views.ForGetPwd.as_view()),  # 忘记密码接口
    path('thirdLog/', views.ThirdPartAPIView.as_view()),  # 三方登录接口
    path('showCourse/', views.ShowCoursesAPIView.as_view()),  # 首页展示课程
    path('path/', views.PathDetailAPIView.as_view()),  # 获取路径详情页数据
    path('webssh/', views.webssh),  # terminal
    path('pay/', pay.page1),  # 获取会员支付页面的url
    path('mypath/', views.MyPath.as_view()),  # 我的路径
    path('mycoupon/', views.MyCoupon.as_view()),  # 我的优惠券
    path('user/', views.UserInfoAPIView.as_view()),  # 用户基本信息
    path('memberOrder/', views.MemberOrderAPIView.as_view()),  # 会员订单
    path('courseOrder/', views.OrderRecordAPIView.as_view()),
    path('sk/', views.SkAPIView.as_view()),  # 秒杀
    path('submit/', views.SubmitAddComment.as_view()),  # 添加读取评论
    path('recommend/', views.RecommendAPIView.as_view()),
    path('uploadcourse/', views.UploadCourse.as_view()),
    path('mySiteMessage/', views.UserSiteMessageAPIView.as_view()),
    path('richText/', views.RichTextAPIView.as_view())

]
