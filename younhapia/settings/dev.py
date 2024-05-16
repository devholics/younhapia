"""
Django settings for younhapia project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from .common import *  # noqa

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "localhost:3000"]

CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]

ROOT_URLCONF = "younhapia.urls.dev"

LOGIN_REDIRECT_URL = "http://localhost:3000"
