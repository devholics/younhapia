from importlib import import_module

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def _get_secret(request):
    if settings.CSRF_USE_SESSIONS:
        return request.session.get(settings.CSRF_SESSION_KEY)
    return request.COOKIES.get(settings.CSRF_COOKIE_NAME)


class UserSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        engine = import_module(settings.SESSION_ENGINE)
        self.SessionStore = engine.SessionStore

    def __call__(self, request):
        if not hasattr(request, "session"):
            raise ImproperlyConfigured(
                "The Django session middleware must be installed prior to this."
            )
        session_token = request.headers.get("x-session-token")
        if session_token is not None:
            # Requests with session token is considered safe.
            # We bypass CSRF protection to use SessionAuthentication.
            request.session = self.SessionStore(session_token)
            secret = _get_secret(request)
            if secret:
                request.META[settings.CSRF_HEADER_NAME] = secret

        request.session.user_agent = request.META.get("HTTP_USER_AGENT", "")
        request.session.ip = request.META.get("REMOTE_ADDR", "")
        return self.get_response(request)
