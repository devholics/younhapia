from django.conf import settings
from django.test import Client, TestCase
from django.urls import reverse

from ..models import User


class AuthenticationTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.staff = User.objects.create_user(
            username="younha", password="holic", is_staff=True
        )
        cls.user = User.objects.create_user(username="riever", password="holic")

    def setUp(self):
        self.app_client = Client(enforce_csrf_checks=True)

    def test_staff_login_admin(self):
        login_url_with_next = f"{settings.LOGIN_URL}?next={reverse("admin:index")}"
        response = self.client.get(reverse("admin:index"))
        self.assertRedirects(response, login_url_with_next)
        response = self.client.post(
            login_url_with_next, {"login": "younha", "password": "holic"}, follow=True
        )
        self.assertRedirects(response, reverse("admin:index"))

    def test_user_login_admin(self):
        login_url_with_next = f"{settings.LOGIN_URL}?next={reverse("admin:index")}"
        response = self.client.get(reverse("admin:index"))
        self.assertRedirects(response, login_url_with_next)
        response = self.client.post(
            login_url_with_next, {"login": "riever", "password": "holic"}, follow=True
        )
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)

    def test_csrf_check_ok(self):
        response = self.app_client.get(reverse("admin:index"), follow=True)
        login_page = response.redirect_chain[-1][0]
        csrf_token = self.app_client.cookies["csrftoken"].value
        response = self.app_client.post(
            login_page,
            {
                "login": "younha",
                "password": "holic",
                "csrfmiddlewaretoken": csrf_token
            },
            follow=True
        )
        self.assertRedirects(response, reverse("admin:index"))

    def test_csrf_check_fail(self):
        response = self.app_client.get(reverse("admin:index"), follow=True)
        login_page = response.redirect_chain[-1][0]
        response = self.app_client.post(
            login_page,
            {
                "login": "younha",
                "password": "holic",
            },
            follow=True,
            headers={
                "x-session-token": "whatever"
            }
        )
        self.assertEqual(response.status_code, 403)
