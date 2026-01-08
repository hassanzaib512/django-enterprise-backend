from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views
from .views import EmailTokenObtainPairView

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", EmailTokenObtainPairView.as_view(), name="login"),
    path("refresh", TokenRefreshView.as_view(), name="refresh"),
    path("me", views.me, name="me"),
]
