from .common import *

DEBUG = False

ALLOWED_HOSTS = ["admin", "api", "auth", "www", "static"]

ROOT_URLCONF = "younhapia.urls.www"

GLOBAL_LOGIN_URL = "//auth/accounts/login/"
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "//www/"

WAGTAIL_FRONTEND_LOGIN_URL = "/login/"

STATIC_HOST = "static"
STATIC_URL = "//static/"
STATIC_ROOT = BASE_DIR / "assets/static"
MEDIA_ROOT = BASE_DIR / "assets/media"
MEDIA_URL = "/media/"

WHITENOISE_USE_FINDERS = True
