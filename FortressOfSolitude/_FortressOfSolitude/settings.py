"""
Django settings for _FortressOfSolitude project.

Based on by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import posixpath
import sys
import os
path_to_here = os.path.dirname(__file__)
sys.path.append(path_to_here)
from _FortressOfSolitude import superhero
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'PLEASE_UPDATE_TO_YOUR_OWN_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '_FortressOfSolitude.organizer',
    '_FortressOfSolitude.Blog',
    '_FortressOfSolitude.superhero',
    '_FortressOfSolitude.NeutrinoKey',
    '_FortressOfSolitude.core',
    'ckeditor',
]
DATABASE_ROUTERS = [
    '_FortressOfSolitude.NeutrinoKey.models.KryptonianSpeak'
]
# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '_FortressOfSolitude.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
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

WSGI_APPLICATION = '_FortressOfSolitude.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),#TODO:ADD YOUR PASSWORD
        'PASSWORD': 'CHANGE_ME',
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = "/" + posixpath.join(*(BASE_DIR.split(os.path.sep) + ['_FortressOfSolitude/superhero/static']))
static_DIR = (
    os.path.join(BASE_DIR, "_FortressOfSolitude/superhero/static"),
    )
print(static_DIR)
print(STATIC_ROOT)
print(BASE_DIR)
from django.urls import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('organizer_tasking_create')
LOGIN_URL = reverse_lazy('dj-auth:login')
LOGOUT_URL = reverse_lazy('dj-auth:logout')

AUTH_USER_MODEL = 'superhero.User'

#HTTPS redirect
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# DAILY_PLANET_PUBLIC_ENCRYPTION
DAILY_PLANET_AES_DEK = b"U\x18yJ\x95a'\xf7\xaa\xff\x92\x8b\x9f\x9a\xc6\xbc\x92\xec;\xac\x9eY\xa0\x84\x9e\xb0\x93\xa5\x95bbC\xf8\xa7\xe8N\x1b\xc3h\xb8\x9ex\xdaf\x7f\xda\xf8\x97\x96jpK\nY\xad\xf5.\x1d\x16q\xe9.xHMa\xa1KzTT%\x16f\x99\xc7\xec[\xfb\xe7~\x14\x1fe\xd5\x1d\x19PG\xdb\xa6\x0b\x85'\x80&\xe3j\x99`\xee\x1f$>\x91^G\xf0\x8f-<e\x10\xd8\xa8\xf9]\xealyD1\xddz\xdd\xdb~\x9a\xb5NtB\x8cI&8\x94_\xae\x99\xc3\x86f\x83<\xb7\xfbK\xe5\xed\xbao~\x99+\x97\x94\xca\x0b\xfe\xa9\x9b\x02`\x83\xbe\x07[\xe5\x9e^\x1a\xed\x00\xb1\xf3d#;\xbb\x122\x9d\xbc=a\x0c\x00\xf1`\x13sgy\x11\xbbW\xcf\xe8h\xde\x8f\xcc\xc1\x81\xdd\xb0n\x83\x16\xf4\xe34\xf6% \xfe\xf7P\x15\xf8\xa3\xa1\xff\xb4\x9c\xc6\xfeB\xba\xf0\xcb~\xc4J\xe6AP\xbb\xee\xd0\x10\xc9\xc5\xb8I\xcc`4\x16\xe4V\xda\xca\x95\xdf"