from rest_framework import authentication

from allauth.usersessions.models import UserSession


class UserSessionAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        session_token = request.headers.get('x-session-token')
        if session_token:
            try:
                session = UserSession.objects.get(token=session_token)
                if not session.purge():
                    user = session.user
                    if user and user.is_active:
                        return user, None
            except UserSession.DoesNotExist:
                return None
