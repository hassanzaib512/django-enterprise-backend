import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


def test_admin_ping_forbidden_for_user():
    client = APIClient()
    client.post(
        "/api/v1/auth/register",
        {"email": "user@example.com", "password": "testpass123"},
        format="json",
    )
    login_response = client.post(
        "/api/v1/auth/login",
        {"email": "user@example.com", "password": "testpass123"},
        format="json",
    )
    access_token = login_response.json()["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get("/api/v1/admin/ping")
    assert response.status_code == 403


def test_admin_ping_allows_admin():
    client = APIClient()
    User = get_user_model()
    user = User.objects.create_user(
        username="admin@example.com",
        email="admin@example.com",
        password="testpass123",
    )
    user.profile.role = "ADMIN"
    user.profile.save()

    login_response = client.post(
        "/api/v1/auth/login",
        {"email": "admin@example.com", "password": "testpass123"},
        format="json",
    )
    access_token = login_response.json()["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get("/api/v1/admin/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "admin pong"}
