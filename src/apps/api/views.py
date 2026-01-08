from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.accounts.permissions import IsAdmin


@api_view(["GET"])
def ping(_request):
    return Response({"message": "pong"})


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsAdmin])
def admin_ping(_request):
    return Response({"message": "admin pong"})
