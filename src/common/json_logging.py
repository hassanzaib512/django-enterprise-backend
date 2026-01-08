import json
import logging
from datetime import UTC, datetime

from .logging_context import get_request_id


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "timestamp": datetime.now(UTC).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        request_id = get_request_id()
        if request_id:
            payload["request_id"] = request_id

        if record.exc_info:
            exc_type = record.exc_info[0].__name__ if record.exc_info[0] else "Exception"
            exc_value = record.exc_info[1]
            payload["exc_info"] = f"{exc_type}: {exc_value}"

        return json.dumps(payload, ensure_ascii=False)
