from uuid import uuid4
from datetime import datetime, timezone


def uuid_id() -> str:
    return str(uuid4())


def current_datetime_str() -> str:
    return datetime.now(timezone.utc).isoformat()
