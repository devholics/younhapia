from urllib.parse import urlparse, urlunparse

from django.conf import settings
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url

REDIRECT_FIELD_NAME = "next"


def login_gateway(request):
    querystring = request.GET.copy()
    next_url = querystring.get(REDIRECT_FIELD_NAME)
    if next_url is not None:
        querystring[REDIRECT_FIELD_NAME] = request.build_absolute_uri(next_url)

    login_url = getattr(settings, "GLOBAL_LOGIN_URL", settings.LOGIN_URL)
    resolved_url = resolve_url(login_url)
    login_url_parts = list(urlparse(resolved_url))
    querystring.update(QueryDict(login_url_parts[4], mutable=True))
    login_url_parts[4] = querystring.urlencode(safe="/")

    return HttpResponseRedirect(urlunparse(login_url_parts))
