from rest_framework.authentication import SessionAuthentication

from .usersessions.utils import get_session_token


class UserSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        # If session token is present, and we are checking CSRF token,
        # then the user is already authenticated with this header and thus
        # further CSRF protection is unnecessary.
        if get_session_token(request) is None:
            return super().enforce_csrf(request)
