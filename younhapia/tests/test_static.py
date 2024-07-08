import pytest


def test_static(client):
    robots_txt = "//static/robots.txt"
    response = client.get(robots_txt)
    assert response.status_code == 200


def test_static_bad(client):
    random_file = "//static/bad.txt"
    response = client.get(random_file)
    assert response.status_code == 404


def test_static_bad_route(client):
    route = "//static/"
    response = client.get(route)
    assert response.status_code == 404
