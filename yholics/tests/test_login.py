import pytest


def _redirect_url(response):
    url = response.redirect_chain[-1][0]
    return url


@pytest.fixture(autouse=True)
def staff_and_user(user_factory):
    user_factory(username="younha", password="holic", is_staff=True)
    user_factory(username="riever", password="holic")


def test_staff_login_admin(client, admin_index_url):
    response = client.get(admin_index_url, follow=True)
    response = client.post(
        _redirect_url(response),
        {"login": "younha", "password": "holic"},
        follow=True,
    )
    assert response.status_code == 200
    assert _redirect_url(response) == admin_index_url


def test_user_login_admin(client, admin_index_url, settings):
    response = client.get(admin_index_url, follow=True)
    response = client.post(
        _redirect_url(response),
        {"login": "riever", "password": "holic"},
        follow=True,
    )
    assert _redirect_url(response) == settings.LOGIN_REDIRECT_URL


def test_csrf_check_ok(secure_client, admin_index_url):
    response = secure_client.get(admin_index_url, follow=True)
    login_page = _redirect_url(response)
    csrf_token = secure_client.cookies["csrftoken"].value
    response = secure_client.post(
        login_page,
        {"login": "younha", "password": "holic", "csrfmiddlewaretoken": csrf_token},
        follow=True,
    )
    assert response.status_code == 200
    assert _redirect_url(response) == admin_index_url


def test_csrf_check_fail(secure_client, admin_index_url):
    response = secure_client.get(admin_index_url, follow=True)
    login_page = response.redirect_chain[-1][0]
    response = secure_client.post(
        login_page,
        {
            "login": "younha",
            "password": "holic",
        },
        follow=True,
        headers={"x-session-token": "whatever"},
    )
    assert response.status_code == 403
