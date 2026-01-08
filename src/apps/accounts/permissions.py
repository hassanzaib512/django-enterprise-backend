from rest_framework.permissions import BasePermission

from .models import UserProfile


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        profile = getattr(user, "profile", None)
        if not user or not user.is_authenticated or not profile:
            return False
        return profile.role == UserProfile.Role.ADMIN


class IsManagerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        profile = getattr(user, "profile", None)
        if not user or not user.is_authenticated or not profile:
            return False
        return profile.role in {UserProfile.Role.ADMIN, UserProfile.Role.MANAGER}
