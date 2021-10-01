from uuid import uuid4
from datetime import datetime, timezone
from dataclasses import fields


def uuid_id() -> str:
    return str(uuid4())


def current_datetime_str() -> str:
    return datetime.now(timezone.utc).isoformat()


def create_class_from_required_fields(cls, source: dict):
    class_required_fields = set([field.name for field in fields(cls)])
    return cls(**{
        key: value for key, value in source.items() if key in class_required_fields
    })
