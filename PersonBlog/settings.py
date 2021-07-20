"""
Django settings for PersonBlog project.

Generated by 'django-admin startproject' using Django 2.2.19.

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
SECRET_KEY = 'h&^%&das298735*&%^(kjgldfbgolijhsdoijfhgshedfgblkjseb6q&w*f)jp40c=&58%687y3'

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
    'rest_framework',
    'rest_framework_jwt',
    'apps.blog.apps.BlogConfig',
    'apps.api.apps.ApiConfig',
    'apps.oauth.apps.OauthConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.auth.LoginMiddleware',
]

ROOT_URLCONF = 'PersonBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'PersonBlog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# 配置自定义用户
AUTH_USER_MODEL = 'blog.UserInfo'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 管理员账号
ADMIN_ACCOUNT = ['test@email.com']

# 腾讯云对象存储
TENCENT_SECRET_ID = 'xxx'
TENCENT_SECRET_KEY = 'xxx'

# 访客白名单
VISITOR_WHITE_FUNCTION = [
    '',
    'detail',
    'register',
    'login',
    'logout',
    'profile',
    'category',
    'oauth',
    'api',
]

# 访客注册账号存储桶
TENCENT_BUCKET = 'PersonBlog-visitor-1305490799'
TENCENT_REGION = 'ap-shanghai'

# 静态文件搜集
STATIC_ROOT = 'xxx'

# rest_framework 配置文件
REST_FRAMEWORK = {

    # 分页配置
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,

    # 生成api文档
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

    # 配置版本
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    "ALLOWED_VERSIONS": ['v1'],
}

# JWT登录过期时间
import datetime

JWT_AUTH = {
    # 登录超时时间
    "JWT_EXPIRATION_DELTA": datetime.timedelta(hours=2),
}

# 请求头
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56",
    "X-Auth-Token": None
}

# 语雀账户Token
YUQUE_TOKEN = "xxxxxxx"

# 配置缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 配置session存储到缓存中
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# 微博授权
WEIBO_CLIENT_ID = "xxx"
WEIBO_CLIENT_SECRET = "xxxx"
WEIBO_CALL_BACK_URL = "/oauth/weibo/response"

# 配置日志
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'log/info.log',
        },
        'warning': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'log/warning.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['info', 'warning'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# 生成环境配置
try:
    from setup import *
except NotImplementedError:
    pass

# 开发环境配置
try:
    from blog_secret_key import *
except NotImplementedError:
    pass
