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

app_name = 'reception'
urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),  # 登录
    path('reg/', views.RegAPIView.as_view()),  # 注册
    path('getimagecode/', views.GetImageCode),  # 获取验证码图片
    path('forgetpwd/', views.ForGetPwd.as_view()),  # 忘记密码接口
    path('thirdLog/', views.ThirdPartAPIView.as_view()),  # 三方登录接口
    path('showCourse/', views.ShowCoursesAPIView.as_view()),
    path('path/', views.PathDetailAPIView.as_view()),
    # path('course/', views.CourseDetailAPIView.as_view())
]
