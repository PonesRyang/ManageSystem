"""
Django settings for ManageSystem project.

Generated by 'django-admin startproject' using Django 2.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1g+tj^0a@tjkh5j9b+t!d!%$5j&#=o%&uitw#9m@mjp*ehlm2&'

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
    'port',
    'window',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'port.middlewares.login_authentication_middleware',
]

# EXCLUDE_URL = (
#     'login/',
#     'logout/',
# )

ROOT_URLCONF = 'ManageSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'ManageSystem.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ManageSystem',
        'HOST': '47.102.219.72',
        'RORT': '3306',
        'USER': 'root',
        'PASSWORD': 'Fengliang96.07.26',
        'TTME_ZONE': 'Asia/Chongqing'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Chongqing'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'api.auths.AllowGetAuthentication',
    #     'api.auths.CustomAuthentication',
    # ),
    # # 配置默认权限
    # "DEFAULT_PERMISSION_CLASSES": (
    #     "api.auths.CustonAythorization",
    # ),
}

CACHES = {
    'default': {
        # 使用第三方库django_redis提供缓存服务支撑
        'BACKEND': 'django_redis.cache.RedisCache',
        # 配置缓存服务器的URL
        'LOCATION': ['redis://47.102.219.72:6379/2', ],
        # 配置缓存的前缀
        'KEY_PREFIX': 'default',
        # 设置缓存相关选项
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 128,
            },
            'PASSWORD': 'fly0726zz',

        }
    },
    'session': {
        # 使用第三方库django_redis提供缓存服务支撑
        'BACKEND': 'django_redis.cache.RedisCache',
        # 配置缓存服务器的URL
        'LOCATION': ['redis://47.102.219.72:6379/1', ],
        # 配置缓存的前缀
        'KEY_PREFIX': 'session',
        # 设置缓存相关选项
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 128,
            },
            'PASSWORD': 'fly0726zz',

        }
    },
}

# 配置将会话放到缓存中
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# 配置使用哪一组缓存来放置会话对象
SESSION_CACHE_ALIAS = 'session'
# 配置会话的超时时间为1天（86400秒）
SESSION_COOKIE_AGE = 86400
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

REST_FRAMEWORK_EXTENSIONS = {
    # 默认的缓存超时时间
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 300,
    # 默认使用哪一组缓存
    'DEFAULT_USE_CACHE': 'default',
    # 配置默认缓存单个对象的key函数
    'DEFAULT_OBJECT_CACHE_KEY_FUNC': 'rest_framework_extensions.utils.default_object_cache_key_func',
    # 配置默认缓存对象列表的key函数
    'DEFAULT_LIST_CACHE_KEY_FUNC': 'rest_framework_extensions.utils.default_list_cache_key_func',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

# DEBUG < INFO < WARNING < ERROR < FATAL
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # 配置日志格式化器
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(module)s.%(funcName)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'verbose': {
            'format': '%(asctime)s %(levelname)s [%(process)d-%(threadName)s] '
                      '%(module)s.%(funcName)s line %(lineno)d: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    # 配置日志过滤器
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 配置日志处理器
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'formatter': 'simple',
        },
        'file1': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'access.log',
            'when': 'W0',
            'backupCount': 12,
            'formatter': 'simple',
            'level': 'INFO',
        },
        'file2': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'error.log',
            'when': 'D',
            'backupCount': 31,
            'formatter': 'verbose',
            'level': 'WARNING',
        },
    },
    # 配置日志器
    'loggers': {
        'django': {
            'handlers': ['console', 'file1', 'file2'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}
