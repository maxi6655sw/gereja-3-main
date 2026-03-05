"""
Development settings for gereja_yp2 project.
Use this for local development only.
"""

from .base import *  # noqa: F401, F403

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-so9v6za(_jti#_+ix)kv875p88nj)@5#t*h^suaqi_3o4x#lsw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # noqa: F405
    }
}
