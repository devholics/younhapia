from django.conf import settings
from django.contrib import admin

from django_hosts import host

host_patterns = [
    host(r"admin", admin.site.urls, name="admin"),
    host(r"api", "younhapia.urls.api", name="api"),
    host(r"auth", "younhapia.urls.auth", name="auth"),
    host(r"www", settings.ROOT_URLCONF, name="www"),
]
