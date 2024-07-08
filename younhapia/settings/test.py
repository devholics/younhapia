from .common import *

DEBUG = False

ALLOWED_HOSTS = ["admin", "api", "auth", "www"]

ROOT_URLCONF = "younhapia.urls.www"

GLOBAL_LOGIN_URL = "//auth/accounts/login/"
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "//www/"

WAGTAIL_FRONTEND_LOGIN_URL = "/login/"

STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"
