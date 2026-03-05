"""
Production settings for gereja_yp2 project.
Configure these before deploying to production.
"""

from .base import *  # noqa: F401, F403
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# Database - use env variables in production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # noqa: F405
        # For PostgreSQL, replace with:
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': os.environ.get('DB_NAME', ''),
        # 'USER': os.environ.get('DB_USER', ''),
        # 'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        # 'HOST': os.environ.get('DB_HOST', 'localhost'),
        # 'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Security
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Static files for production
STATIC_ROOT = BASE_DIR / 'staticfiles'  # noqa: F405
