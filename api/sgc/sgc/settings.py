import os
import mongoengine
import requests 
import datetime 

"""
Django settings for sgc project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f7o3wfiz*7co-h$ci2c8-+g(%e^t_zm+5c5^tqxljb^!qmvq^&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
PROD_ENV = False
COMMENTS = False
ALLOWED_HOSTS = ['mysite.com', '127.0.0.1', '*']


if PROD_ENV:
    EC2_PRIVATE_IP = None
    try:
        EC2_PRIVATE_IP = requests.get(
            'http://169.254.169.254/latest/meta-data/public-hostname',
            timeout=0.01).text
    except requests.exceptions.RequestException:
        pass

    if EC2_PRIVATE_IP:
        ALLOWED_HOSTS.append(EC2_PRIVATE_IP)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'core',
    'projeto',
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

ROOT_URLCONF = 'sgc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'sgc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if not PROD_ENV:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django',
            'USER': 'rodrigo',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '5432',
        }        
    }


if COMMENTS:
    mongo_host = '127.0.0.1' 
    mongo_port = 27017
    mongo_database = 'comments'
    mongoengine.connect(mongo_database, host=mongo_host, port=mongo_port)

    #DATABASES['mongodb'] = {
    #    'ENGINE': 'django_mongodb_engine',
    #    'NAME': 'comments',
    #    'USER': 'root',
    #    'PASSWORD': 'root',
    #    'HOST': 'localhost',
    #}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

LOGIN_REDIRECT_URL = 'projeto:listar'
LOGOUT_URL = 'logout'
LOGIN_URL = 'login'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'core.authentication.EmailAuthBackend',
    'social_core.backends.google.GoogleOAuth2'
]


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '179227412138-qj5mir02b8ea8iuv24k5js6864dqgir1.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'g5jwJpOl5VYdbkQdqDeL3xPV'


REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

#https://www.jetbrains.com/pycharm/guide/tutorials/django-aws/rest-api-jwt/
#https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=2),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',
}
