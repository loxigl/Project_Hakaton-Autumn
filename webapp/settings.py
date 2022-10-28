"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os.path
from pathlib import Path
import mimetypes

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.template.backends import django

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-&!)dmjs9)=yq-e6n_h_u)s1nimtqauks@=4#kl$^mu%j30a&^s')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DJANGO_DEBUG', False))

ALLOWED_HOSTS = [
  '127.0.0.1',
  'hackathon-autumun.herokuapp.com'
]

# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'web.apps.WebConfig',
  'user.apps.UserConfig',
  'news.apps.NewsConfig',
  'ckeditor',
  'ckeditor_uploader',
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

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
      # for prod
      BASE_DIR / 'build/template',

      # for dev
      BASE_DIR / 'source/templates',

    ]
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

WSGI_APPLICATION = 'webapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
  'default': {'ENGINE': 'django.db.backends.postgresql',
              'HOST': os.environ.get('POSTGRES_HOST', 'ec2-54-160-200-167.compute-1.amazonaws.com'),
              'NAME': os.environ.get('POSTGRES_DB', 'dbp2fprm2mlte7'),
              'USER': os.environ.get('POSTGRES_USER', 'nwbzgggruzhrqn'),
              'PASSWORD': os.environ.get('POSTGRES_PASSWORD',
                                         '711e8d846024b575a49bceaec9aecea09d7ccf9b572c40f7866257c5bf9eb159'),
              'PORT': os.environ.get('POSTGRES_PORT', '5432'), },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'
DATE_FORMAT = 'j-m-y'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')
MEDIA_URL = '/media/'
STATIC_URL = 'static/'
# Redirect to home URL after login (Default redirects to /accounts/profile/)
AUTH_USER_MODEL = 'user.User'
AUTHENTICATION_BACKENDS = ['user.backend.UserBackend']
# for production
STATIC_ROOT = os.path.join(BASE_DIR / 'build/static')

# for dev
# STATIC_ROOT = os.path.join(BASE_DIR / 'source')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'rector.site@gmail.com'
EMAIL_HOST_PASSWORD = 'otdxtomrqyicsoxw'
EMAIL_USE_TLS = True
CKEDITOR_UPLOAD_PATH = 'uploads/'
# CKEDITOR_CONFIGS
CKEDITOR_CONFIGS = {
  'default': {
    'toolbar': [
      ['Undo', 'Redo',
       '-', 'Bold', 'Italic', 'Underline',
       '-', 'Link', 'Unlink', 'Anchor',
       '-', 'Format',
       '-', 'Maximize',
       '-', 'Table',
       '-', 'Image',
       '-', 'Source',
       '-', 'NumberedList', 'BulletedList'
       ],
      ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
       '-', 'Font', 'FontSize', 'TextColor',
       '-', 'Outdent', 'Indent',
       '-', 'HorizontalRule',
       '-', 'Blockquote'
       ]
    ],
    'height': 500,
    'width': '100%',
    'toolbarCanCollapse': False,
    'forcePasteAsPlainText': True
  },
  'comment': {
    'toolbar': [
    ],
    'height': 80,
    'width': 500,
    'forcePasteAsPlainText': True
  }
}