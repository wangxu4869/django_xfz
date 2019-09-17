"""
Django settings for XFZ project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+fvt@of7xo7i)&d!)m5v@$o59jf_bue$ukxs*^mq$!9uv!r3dj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['47.240.61.183']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.news',
    'apps.cms',
    'apps.xfzauth',
    'apps.course',
    'apps.ueditor',
    'rest_framework',
    'apps.payinfo',
    'haystack'
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

ROOT_URLCONF = 'XFZ.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'front','templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins':[
                'django.templatetags.static'
            ]
        },
    },
]

WSGI_APPLICATION = 'XFZ.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xfz',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'root'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL='xfzauth.User'

#缓存配置
CACHES={
    'default':{
        'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION':'127.0.0.1:11211'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static_dist')
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'front','dist')
]

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')


# Qiniu配置
QINIU_ACCESS_KEY = '9-7_e1Ib_BMkgbdsSgmpGoW_VIrTYMGKO-3XdxtG'
QINIU_SECRET_KEY = 'FzvqhdlgxRaOw5Kh2CvmrJkce8-s-e1Aq9wl7S0h'
QINIU_BUCKET_NAME = 'wxvideo'
QINIU_DOMAIN = 'http://82c43q.s3-cn-east-1.qiniucs.com'

# 七牛和自己的服务器，最少要配置一个
# UEditor配置
UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = QINIU_ACCESS_KEY
UEDITOR_QINIU_SECRET_KEY = QINIU_SECRET_KEY
UEDITOR_QINIU_BUCKET_NAME = QINIU_BUCKET_NAME
UEDITOR_QINIU_DOMAIN = QINIU_DOMAIN


UEDITOR_UPLOAD_TO_SERVER=True
UEDITOR_UPLOAD_PATH=MEDIA_ROOT
UEDITOR_CONFIG_PATH=os.path.join(BASE_DIR,'front','dist','ueditor','config.json')


#一次加载多少篇文章
ONE_PAGE_NEWS_COUNT=2

#百度云的配置
#控制台-》用户中心-》用户ID
BAIDU_CLOUD_USER_ID='3fa4c508eef44bf49fafc96aec53117d'
# 点播VOD-》全局设置-》发布设置-》安全设置-》Userkey
BAIDU_CLOUD_USER_KEY='8956c440a18745ed'

HAYSTACK_CONNECTIONS={
    'default':{
        #设置haystack的搜索引擎
        'ENGINE':'haystack.backends.whoosh_backend.WhooshEngine',
        #设置索引文件位置
        'PATH':os.path.join(BASE_DIR,'whoosh_index'),
    }
}