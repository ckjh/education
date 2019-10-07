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
from admin01 import views

app_name = 'admin01'
urlpatterns = [
    path('tag/', views.TagAPIView.as_view()),  # 课程标签管理
    path('level/', views.LevelAPIView.as_view()),  # 会员等级管理
    path('condition/', views.ConditionAPIView.as_view()),  # 会员条件管理
    path('siteMessage/', views.SiteMessageAPIView.as_view()),  # 站内信管理
    path('path/', views.PathAPIView.as_view()),  # 路径管理
    path('stage/', views.PathstageView.as_view())
]
