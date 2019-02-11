# -*- coding: utf-8 -*-
"""
Django settings for my_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(*#$ech#_s8z7)27%7+^(&swl%#*o7_bfle5w8d2m6w-(#34jn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',          # бекенд авторизации через ВКонтакте
    'django.contrib.auth.backends.ModelBackend', # бекенд классической аутентификации, чтобы работала авторизация через обычный логин и пароль
)

ROOT_URLCONF = 'my_project.urls'

WSGI_APPLICATION = 'my_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

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
                'social_django.context_processors.backends', # Добавил эту строку
                'my_project.context_processors.get_settings',
            ],
        },
    },
]

#TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates'),]

SOCIAL_AUTH_VK_OAUTH2_KEY = '6725913'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'QlxBohwZTCAJFQVXAi1J'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['friends']

#OAUTH_TOKENS_HISTORY = True # to keep in DB expired access tokens
#OAUTH_TOKENS_VKONTAKTE_CLIENT_ID = '6725913' # application ID
#OAUTH_TOKENS_VKONTAKTE_CLIENT_SECRET = 'QlxBohwZTCAJFQVXAi1J' # application secret key
#OAUTH_TOKENS_VKONTAKTE_SCOPE = ['friends'] # application scopes
#OAUTH_TOKENS_VKONTAKTE_USERNAME = '' # user login
#OAUTH_TOKENS_VKONTAKTE_PASSWORD = '' # user password
#OAUTH_TOKENS_VKONTAKTE_PHONE_END = '' # last 4 digits of user mobile phone


LOGIN_REDIRECT_URL = '/'
