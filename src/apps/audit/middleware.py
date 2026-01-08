from time import perf_counter
from uuid import uuid4

from common.logging_context import set_request_id

from .models import AuditLog


class AuditLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_id = uuid4()
        request.request_id = request_id
        set_request_id(str(request_id))
        start_time = perf_counter()

        response = None
        try:
            response = self.get_response(request)
            return response
        finally:
            if response is not None:
                response["X-Request-ID"] = str(request_id)
                duration_ms = int((perf_counter() - start_time) * 1000)

                try:
                    user = request.user if getattr(request, "user", None) else None
                    if user and not user.is_authenticated:
                        user = None
                    AuditLog.objects.create(
                        request_id=request_id,
                        user=user,
                        method=request.method,
                        path=request.path,
                        status_code=response.status_code,
                        duration_ms=duration_ms,
                    )
                except Exception:
                    pass
            set_request_id(None)
