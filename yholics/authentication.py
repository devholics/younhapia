from rest_framework import authentication


class UserSessionAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        session_token = request.headers.get("x-session-token")
        # CSRF attack prevention
        if session_token == request.session.session_key:
            user = request.user
            if user.is_authenticated and user.is_active:
                return user, None
