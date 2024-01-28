"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv
import redis
import logging


logger = logging.getLogger(__name__)



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4tsg-$_m6v0*j!9+0ho*7g1!!55649cxp&_e)@e%ytl!ge8m=k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news.apps.NewsConfig',
    'accounts',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',
    'sign',
    'protect',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_apscheduler',
]


SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'NewsPaper.urls'

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

AUTHENTICATION_BACKENDS = [
    # Needed to log in by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}
ACCOUNT_CONFIRM_EMAIL_ON_GET = True


WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# LOGIN_URL = 'sign/login/'
# LOGIN_REDIRECT_URL = '/

# load_dotenv()

SITE_URL = 'http://127.0.0.1:8000'
EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковы
EMAIL_HOST_USER = 'd.agur'
EMAIL_HOST_PASSWORD = 'eexpuoqeihoolxms'

EMAIL_USE_SSL = 'True'
DEFAULT_FROM_EMAIL = 'd.agur@yandex.ru'
SERVER_EMAIL = 'd.agur@yandex.ru'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25
# Через РедисЛабс
# CELERY_BROKER_URL = 'redis://:Vet7nJ0FXRSmQBLTqvRmYlEw9pYjbES3@redis-17393.c228.us-central1-1.gce.cloud.redislabs.com:17393/0'
# CELERY_RESULT_BACKEND = 'redis://:Vet7nJ0FXRSmQBLTqvRmYlEw9pYjbES3@redis-17393.c228.us-central1-1.gce.cloud.redislabs.com:17393/0'
# Через Редис и Линукс
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']  # допустимый формат данных.
CELERY_TASK_SERIALIZER = 'json'  # метод сериализации задач.
CELERY_RESULT_SERIALIZER = 'json'  # метод сериализации результатов.

# 16 ЮНИТ
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'style': '{',
    # --Блок определения формата сообщений для опр. уровня
    'formatters': {
        'simple': {          # для стандартных сообщений
            'format': '%(asctime)-8s %(levelname)-8s %(message)s'  # время возникновения сообщения,уровень логирования,само сообщение
        },
        'advanced_path': {  # для сообщений уровня WARNING
            'format': '%(asctime)-8s %(levelname)-8s %(pathname)-8s %(message)s'  # время возникновения сообщения,уровень логирования,путь к источнику события, само сообщение
        },
        'advanced_path_exc': {  # для сообщений ERROR и CRITICAL
            'format': '%(asctime)-8s %(levelname)-8s %(pathname)-8s %(exc_info)-8s %(message)s'  # время возникновения сообщения,уровень логирования,путь к источнику события,стэк ошибки, само сообщение
        },
        'advanced_module': {  # для файлов general.log, уровень INFO
            'format': '%(asctime)-8s %(levelname)-8s %(module)-8s %(message)s'  # время возникновения сообщения,уровень логирования,модуль в котором вознило сообщение,само сообщение
        },
        'security_format': {
            'format': '%(asctime)s %(levelname)s - %(module)s - %(message)s'
        },
    },
    # --Блок фильтров
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    # --Блок вывода сообщений в консоль для опр. уровней
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'advanced_path'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'advanced_path_exc'
        },
        # --Блок вывода сообщений в файл general.log
        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'advanced_module',
            'filename': 'general.log'
        },
        # --Блок вывода сообщений в файл errors.log
        'file_errors': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'advanced_path_exc',
            'filename': 'errors.log',
        },
        # --Блок вывода сообщений в файл security.log
        'file_security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'advanced_module',
            'filename': 'security.log',
        },
        # --Блок для отправки сообщений на почту
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'advanced_path'
        },
    },
    # --Определяем регистраторы
    'loggers': {
        # Регистратор django
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_error', 'file_general'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # Регистратор django.request
        'django.request': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Регистратор django.server
        'django.server': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Регистратор django.template
        'django.template': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Регистратор django.db_backends
        'django.db_backends': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Регистратор django.security
        'django.security': {
            'handlers': ['file_security'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}