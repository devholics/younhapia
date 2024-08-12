import pytest


@pytest.fixture(autouse=True)
def dummy_view(settings):
    settings.ROOT_HOSTCONF = "yholics.tests.hosts"
    settings.ALLOWED_HOSTS += ["dummy"]


@pytest.fixture
def staff(user_factory):
    return user_factory(username="younha", password="holic", is_staff=True)


@pytest.fixture
def dummy_api():
    from django_hosts import reverse

    return reverse("dummy", host="dummy")


def test_session_token_csrf_exempt(secure_client, staff, admin_index_url, dummy_api):
    secure_client.force_login(staff)
    response = secure_client.get(admin_index_url)
    assert response.status_code == 200
    response = secure_client.post(
        dummy_api,
        headers={"x-session-token": secure_client.session.session_key},
    )
    assert response.status_code == 200


def test_session_token_csrf_fails(secure_client, staff, admin_index_url, dummy_api):
    secure_client.force_login(staff)
    response = secure_client.get(admin_index_url)
    assert response.status_code == 200
    response = secure_client.post(dummy_api, headers={"x-session-token": "whatever"})
    assert response.status_code == 403
