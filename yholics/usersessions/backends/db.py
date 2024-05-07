from django.contrib import auth
from django.contrib.sessions.backends.db import SessionStore as DBStore


class SessionStore(DBStore):
    def __init__(self, session_key=None):
        super().__init__(session_key)
        self.user_agent = None
        self.ip = None
        self.user_id = None

    @classmethod
    def get_model_class(cls):
        from ..models import UserSession

        return UserSession

    def __setitem__(self, key, value):
        if key == auth.SESSION_KEY:
            self.user_id = value
        super().__setitem__(key, value)

    def _get_session_from_db(self):
        s = super()._get_session_from_db()
        if s is not None:
            self.user_id = s.user_id
            # In some cases such as SSR, the frontend may not send
            # the user agent and IP information.
            if not self.user_agent:
                self.user_agent = s.user_agent
            if not self.ip:
                self.ip = s.ip
            if self.user_agent != s.user_agent or self.ip != s.ip:
                self.modified = True
        return s

    def create_model_instance(self, data):
        obj = super().create_model_instance(data)
        obj.user_agent = self.user_agent
        obj.user_id = self.user_id
        obj.ip = self.ip
        return obj

    def clear(self):
        super().clear()
        self.user_id = None
