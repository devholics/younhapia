from urllib.parse import urlparse

from django.conf import settings
from django.http import HttpResponseNotFound

from whitenoise.middleware import WhiteNoiseMiddleware


class SupersonicMiddleware(WhiteNoiseMiddleware):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.static_host = getattr(settings, "STATIC_HOST", urlparse(settings.STATIC_URL or "").netloc)

    def __call__(self, request):
        host = request.get_host()
        if self.static_host == host:
            self.get_response = lambda _: HttpResponseNotFound()
        elif self.static_host:
            return self.get_response(request)
        return super().__call__(request)
