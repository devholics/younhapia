from importlib import import_module

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


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
            # If session token is found, it takes precedence over cookies
            # to prevent CSRF attacks.
            request.session = self.SessionStore(session_token)
        request.session.user_agent = request.META.get("HTTP_USER_AGENT", "")
        request.session.ip = request.META.get("REMOTE_ADDR", "")
        return self.get_response(request)
