import pytest
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


def test_register_success():
    client = APIClient()
    response = client.post(
        "/api/v1/auth/register",
        {"email": "user@example.com", "password": "testpass123"},
        format="json",
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["email"] == "user@example.com"


def test_login_success():
    client = APIClient()
    client.post(
        "/api/v1/auth/register",
        {"email": "login@example.com", "password": "testpass123"},
        format="json",
    )
    response = client.post(
        "/api/v1/auth/login",
        {"email": "login@example.com", "password": "testpass123"},
        format="json",
    )
    assert response.status_code == 200
    data = response.json()
    assert "access" in data
    assert "refresh" in data


def test_me_requires_auth():
    client = APIClient()
    response = client.get("/api/v1/auth/me")
    assert response.status_code == 401


def test_me_with_token():
    client = APIClient()
    client.post(
        "/api/v1/auth/register",
        {"email": "me@example.com", "password": "testpass123"},
        format="json",
    )
    login_response = client.post(
        "/api/v1/auth/login",
        {"email": "me@example.com", "password": "testpass123"},
        format="json",
    )
    access_token = login_response.json()["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get("/api/v1/auth/me")
    assert response.status_code == 200
    assert response.json()["email"] == "me@example.com"
