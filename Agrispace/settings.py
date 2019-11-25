"""
Django settings for Agrispace project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from decouple import config
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k4npo=2(dqxih*ib1*yylq$*0ij4bywg880^(&t=&ca-b5f+q6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['localhost','127.0.0.1','ancient-inlet-56922.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.openid',
    'corsheaders',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True  


ROOT_URLCONF = 'Agrispace.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Agrispace.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
if DEBUG == True:
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            # 'HOST':"localhost",
            'NAME':"Agrispace",
            # "PORT": 27017


        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'HOST': 'mongodb://admin:ezwmD9N5qbmawmVE@SG-Agrispace-28152.servers.mongodirector.com:27017/admin',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    "allauth.account.auth_backends.AuthenticationBackend",
    )
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = True
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
# ACCOUNT_SESSION_REMEMBER = None
# ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# ACCOUNT_UNIQUE_EMAIL = True
# # ACCOUNT_EMAIL_VERIFICATION ="optional"
# # ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =3
# # ACCOUNT_CONFIRM_EMAIL_ON_GET=True
# SOCIALACCOUNT_ADAPTER ="allauth.socialaccount.adapter.DefaultSocialAccountAdapter"
# SOCIALACCOUNT_AUTO_SIGNUP =True
# SOCIALACCOUNT_FORMS ={'signup': 'Accounts.forms.SocialForm'}
# SITE_ID = 1
# ACCOUNT_FORMS = {'signup': 'Accounts.forms.MyCustomSignupForm'}
# AUTH_USER_MODEL = 'Accounts.CustomUser'

# SOCIALACCOUNT_PROVIDERS = {
# 'openid': {
# 'SERVERS': [
# dict(id='google',
# name='Google',
# openid_url='https://www.google.com/accounts/o8/id'),
# ]
# }
# }
CORS_ORIGIN_ALLOW_ALL = True