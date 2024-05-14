from rest_framework.authentication import SessionAuthentication


class UserSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        # If session token is present, and we are checking CSRF token,
        # then the user is already authenticated with this header and thus
        # further CSRF protection is unnecessary.
        if not request.META.get('SESSION_TOKEN_USED', False):
            return super().enforce_csrf(request)
