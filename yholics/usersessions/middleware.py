from importlib import import_module

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_session_token(request):
    return request.headers.get("x-session-token")


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
        session_token = get_session_token(request)
        if session_token is not None:
            # Session token takes precedence over session cookie
            # to prevent CSRF attacks.
            request.META["SESSION_TOKEN_USED"] = True
            request.session = self.SessionStore(session_token)

        request.session.user_agent = request.META.get("HTTP_USER_AGENT", "")
        request.session.ip = request.META.get("REMOTE_ADDR", "")
        return self.get_response(request)
