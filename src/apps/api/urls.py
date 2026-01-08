from django.urls import path

from . import views

urlpatterns = [
    path("admin/ping", views.admin_ping, name="admin-ping"),
    path("ping", views.ping, name="ping"),
]
