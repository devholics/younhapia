from django.conf import settings
from django.test import Client, TestCase, override_settings
from django.urls import reverse

from ..models import User


@override_settings(
    ROOT_HOSTCONF="yholics.tests.hosts",
    ROOT_URLCONF="yholics.tests.urls",
)
class UserSessionTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.staff = User.objects.create_user(
            username="younha", password="holic", is_staff=True
        )

    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)

    def _safe_login(self):
        self.client.get(settings.LOGIN_URL)
        csrf_token = self.client.cookies["csrftoken"].value
        response = self.client.post(
            settings.LOGIN_URL,
            {"login": "younha", "password": "holic", "csrfmiddlewaretoken": csrf_token},
            follow=True,
        )
        return response

    def test_session_token_csrf_exempt(self):
        self.client.force_login(self.staff)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse("dummy"),
            headers={"x-session-token": self.client.session.session_key},
        )
        self.assertEqual(response.status_code, 200)

    def test_session_token_csrf_fails(self):
        self.client.force_login(self.staff)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse("dummy"), headers={"x-session-token": "whatever"}
        )
        self.assertEqual(response.status_code, 403)
