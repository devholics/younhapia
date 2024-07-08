from urllib.parse import urlsplit, urlunsplit

from django.test import Client

import pytest


class HostsClient(Client):
    def generic(self, method, path, *args, **extra):
        """Used by all methods."""
        # Populate the host header from the URL host, to play nicely with django-hosts
        parsed_url = urlsplit(path)
        scheme = parsed_url.scheme
        netloc = parsed_url.netloc
        path = urlunsplit(["", ""] + list(parsed_url[2:]))
        if scheme:
            extra["wsgi.url_scheme"] = scheme
        if netloc:
            extra["headers"] = extra["headers"] or {}
            extra["headers"]["host"] = netloc
        return super().generic(method, path, *args, **extra)


@pytest.fixture
def client():
    return HostsClient()


@pytest.fixture
def secure_client():
    return HostsClient(enforce_csrf_checks=True)


@pytest.fixture
def user_factory(django_user_model):
    return django_user_model.objects.create_user


@pytest.fixture
def admin_index_url():
    from django_hosts import reverse

    return reverse("admin:index", host="admin", scheme="http")
