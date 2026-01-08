import uuid

import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from apps.audit.models import AuditLog

pytestmark = pytest.mark.django_db


def test_health_creates_audit_log_and_request_id_header():
    client = APIClient()
    response = client.get("/health")
    assert response.status_code == 200

    request_id = response.headers.get("X-Request-ID")
    assert request_id is not None
    uuid.UUID(request_id)

    assert AuditLog.objects.filter(path="/health", status_code=200).exists()


def test_audit_logs_requires_admin():
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
    response = client.get("/api/v1/admin/audit-logs")
    assert response.status_code == 403


def test_audit_logs_allows_admin():
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
    response = client.get("/api/v1/admin/audit-logs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
