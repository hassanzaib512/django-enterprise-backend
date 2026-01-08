from django.db import connection
from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def health(_request):
    return JsonResponse({"status": "ok"})


@require_GET
def ready(_request):
    try:
        connection.ensure_connection()
    except Exception:
        return JsonResponse({"status": "degraded", "db": "error"})
    return JsonResponse({"status": "ok", "db": "ok"})
