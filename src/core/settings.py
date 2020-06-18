"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from pathlib import Path
from dynaconf import settings as _settings
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent.parent.parent.resolve()
PROJECT_DIR = BASE_DIR / "src" / "core"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = _settings.SECRET_KEY

# %op^bj82udy537)$up7_-bcew4tc_7#e9b_)1vh!7o_m4o*=!r
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = _settings.DEBUG

ALLOWED_HOSTS = _settings.ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'orders',
    'products',
    'search',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'orders.context_processors.getting_basket_info',
                'orders.context_processors.category',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

db_url = _settings.DATABASE_URL
if _settings.ENV_FOR_DYNACONF == "heroku":
    db_url = os.getenv("DATABASE_URL")


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {"default": dj_database_url.parse(db_url, conn_max_age=600)}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT_DIR = BASE_DIR / "static"
STATIC_ROOT_DIR.mkdir(exist_ok=True)
STATIC_ROOT = STATIC_ROOT_DIR.as_posix()

STATIC_URL = "/static/"

STATICFILES_DIRS = [PROJECT_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, "static", "media")
