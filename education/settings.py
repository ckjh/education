"""
Django settings for education project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=#@9(j&m8$)ik-#tew(e#fp4-lkb9)__#+adn&w!sa49#o#5in'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin01.apps.Admin01Config',
    'rest_framework',
    'rest_framework.authtoken',
    'reception',
    'djcelery'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'education.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'education.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '116.62.155.103',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'root',
        'NAME': 'education'
    },
    'slave': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '106.13.222.216',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'root',  # 数据库用户密码
        'NAME': 'education'  # 数据库名字
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 发邮件
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'liujunjie_j@163.com'
EMAIL_HOST_PASSWORD = 'abc123'
EMAIL_FORM = '实验楼<liujunjie_j@163.com>'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
import datetime

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),  # token 过期时间
    # 'JWT_RESPONSE_PAYLOAD_HANDLER': 'user.utils.jwt_response_payload_handler',  # 自定义响应内容,指定user子应用下,的utils.py文件
}

AUTH_USER_MODEL = 'admin01.User'  # 指定用户表
DATABASE_ROUTERS = ['utils.db_router.MasterSlaveRouter']

PIC_URL = 'http://116.62.155.103:8888/'
# DEFAULT_FILE_STORAGE = 'admin01.storage.FastDFSStorage'
SIP = '106.13.222.216'
IP = '116.62.155.103'
USER = 'root'  # 用户名
PASSWORD = 'YTYyty2211'  # 密码

import djcelery

djcelery.setup_loader()
BROKER_URL = 'amqp://username01:password01@116.62.155.103:5672/myvhost'
CELERY_IMPORTS = ('reception.task')  # 任务路径
CELERY_RESULT_BACKEND = 'amqp://hnq:123456@116.62.155.103:5672/myvhost'
CELERY_TIMEZONE = 'UTC'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

APP_KEY = '3345882312'
APP_SECRET = 'f73a866a48b58b0f275111109c265748'
CALLBACK_URL = 'http://127.0.0.1:8080/weibo_callback/'
MemberPayCallBack = "http://127.0.0.1:8000/memberOrder/"
CoursePayCallBack = "http://127.0.0.1:8000/courseOrder/"
UserCenterUrl = 'http://localhost:8080/userCenter'
IndexCenterUrl = 'http://localhost:8080'
