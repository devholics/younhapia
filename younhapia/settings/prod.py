from .common import *

DEBUG = False

ALLOWED_HOSTS = [
    "younhalibrary.com",
    "www.younhalibrary.com",
    "auth.younhalibrary.com",
    "admin.younhalibrary.com",
    "static.younhalibrary.com",
]

ROOT_URLCONF = "younhapia.urls.www"

GLOBAL_LOGIN_URL = "https://auth.younhalibrary.com/accounts/login/"
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "https://www.younhalibrary.com/"

WAGTAIL_FRONTEND_LOGIN_URL = "/login/"

STATIC_HOST = "static.younhalibrary.com"
STATIC_URL = "https://static.younhalibrary.com/"
STATIC_ROOT = BASE_DIR / "assets/static"
MEDIA_ROOT = DATA_DIR / "assets/media"
MEDIA_URL = "/media/"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
