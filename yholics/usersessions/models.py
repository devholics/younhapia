from django.conf import settings
from django.contrib.sessions.base_session import AbstractBaseSession, BaseSessionManager
from django.db import models


class SessionManager(BaseSessionManager):
    use_in_migrations = True


class UserSession(AbstractBaseSession):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE
    )
    user_agent = models.CharField(null=True, blank=True, max_length=200)
    last_activity = models.DateTimeField(auto_now=True)
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="IP")

    objects = SessionManager()

    @classmethod
    def get_session_store_class(cls):
        from .backends.db import SessionStore

        return SessionStore
