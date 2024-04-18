import json
import os
from pathlib import Path

PROJECT_PACKAGE = Path(__file__).resolve().parent.parent

BASE_DIR = PROJECT_PACKAGE.parent

data_dir_key = "YOUNHAPIA_DATA_DIR"
DATA_DIR = (
    Path(os.environ[data_dir_key]) if data_dir_key in os.environ else BASE_DIR.parent
)

try:
    with DATA_DIR.joinpath("conf", "secrets.json").open() as handle:
        SECRETS = json.load(handle)
except IOError:
    SECRETS = {
        "secret_key": "a"
    }


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(SECRETS["secret_key"])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    'rest_framework',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.twitter_oauth2',
    'allauth.usersessions',

    'yholics',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # allauth
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'younhapia.urls'

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

                # allauth
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'younhapia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'younhapia',
        'USER': 'younhapia',
        'HOST': SECRETS.get('db_host', ''),
        'PASSWORD': SECRETS.get('db_password', ''),
        'PORT': SECRETS.get('db_port', ''),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Sites framework
# https://docs.djangoproject.com/en/5.0/ref/contrib/sites/

SITE_ID = 1


# Authentication

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    # allauth
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Custom user model

AUTH_USER_MODEL = 'yholics.User'


# Django REST Framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'yholics.authentication.UserSessionAuthentication',
    ]
}
