from django.urls import reverse

import pytest


def _redirect_url(response):
    url = response.redirect_chain[-1][0]
    return url


@pytest.fixture
def superuser(user_factory):
    return user_factory(username="younha", password="holic", is_superuser=True)


@pytest.fixture
def user(user_factory):
    return user_factory(username="riever", password="holic")


@pytest.fixture
def admin_url():
    return reverse("wagtailadmin_home")


@pytest.fixture
def admin_login_url():
    return reverse("wagtailadmin_login")


@pytest.mark.django_db
def test_admin_urls(client, admin_url, settings):
    response = client.get(admin_url, follow=True)
    assert response.status_code == 200
    assert _redirect_url(response).startswith(settings.GLOBAL_LOGIN_URL)


def test_normal_user(client, admin_url, user, settings):
    # Must avoid redirect loop
    client.force_login(user)
    response = client.get(admin_url, follow=True)
    assert response.status_code == 200
    assert _redirect_url(response) == settings.LOGIN_REDIRECT_URL


def test_superuser(client, admin_url, admin_login_url, superuser):
    client.force_login(superuser)
    response = client.get(admin_login_url, follow=True)
    assert response.status_code == 200
    assert _redirect_url(response) == admin_url


def test_disabled_url(client, admin_url, superuser):
    client.force_login(superuser)
    password_reset_url = f"{admin_url}password_reset/"
    response = client.get(password_reset_url)
    assert response.status_code == 404
