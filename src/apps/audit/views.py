from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.accounts.permissions import IsAdmin

from .models import AuditLog


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsAdmin])
def audit_logs(request):
    limit_param = request.query_params.get("limit", "50")
    try:
        limit = int(limit_param)
    except ValueError:
        limit = 50
    limit = max(1, min(limit, 200))

    logs = AuditLog.objects.order_by("-created_at")[:limit]
    data = [
        {
            "created_at": log.created_at,
            "request_id": log.request_id,
            "user_id": log.user_id,
            "method": log.method,
            "path": log.path,
            "status_code": log.status_code,
            "duration_ms": log.duration_ms,
        }
        for log in logs
    ]
    return Response(data)
