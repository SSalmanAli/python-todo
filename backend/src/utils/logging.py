import logging
from typing import Any
from fastapi import Request
import json


def setup_logging():
    """Set up basic logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )


def log_api_call(request: Request, response: Any = None, user_id: str = None):
    """Log API call details."""
    logger = logging.getLogger(__name__)

    log_data = {
        "method": request.method,
        "url": str(request.url),
        "user_id": user_id,
        "client_host": request.client.host if request.client else None,
        "user_agent": request.headers.get("user-agent"),
    }

    if response:
        log_data["response_status"] = getattr(response, "status_code", "unknown")

    logger.info(f"API Call: {json.dumps(log_data)}")


def get_logger(name: str) -> logging.Logger:
    """Get a configured logger instance."""
    return logging.getLogger(name)