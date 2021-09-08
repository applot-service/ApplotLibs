from dataclasses import dataclass, field
from ApplotLibs.Utilities.helpers import uuid_id, current_datetime_str


@dataclass
class Event:
    event_id: str = field(default_factory=uuid_id)
    event_created_date: str = field(default_factory=current_datetime_str)
    event: str = field(default=False)
    local: bool = field(default=False)


@dataclass
class Command:
    command_id: str = field(default_factory=uuid_id)
    command_created_date: str = field(default_factory=current_datetime_str)
    command: str = field(default=None)
    local: bool = field(default=False)
