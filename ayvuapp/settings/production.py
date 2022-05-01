# For production, check:
# manage.py check --deploy
# https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

from .base import *
import os
import django_heroku

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

PREPEND_WWW = True

CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-failure-view


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  #: On top after security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

# Logging
# https://docs.djangoproject.com/en/4.0/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'WARNING'),
            'propagate': False,
        },
        'ayvuapp': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'WARNING'),
            'propagate': False,
        },
    },
}


# Heroku settings

django_heroku.settings(locals())
