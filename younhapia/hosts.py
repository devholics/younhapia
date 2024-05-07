from django_hosts import host

host_patterns = [
    host(r"admin", "younhapia.urls.admin", name="admin"),
    host(r"api", "younhapia.urls.api", name="api"),
    host(r"auth", "allauth.headless.urls", name="auth"),
    host(r"www", "younhapia.urls.www", name="www"),
]
