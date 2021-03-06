from dataclasses import dataclass, field, asdict, fields
from ApplotLibs.Utilities.helpers import (
    uuid_id,
    current_datetime_str,
    create_class_from_required_fields
)


@dataclass
class Event:
    event_id: str = field(default_factory=uuid_id)
    event_created_date: str = field(default_factory=current_datetime_str)
    event_type: str = field(default=None)  # File name (Account, Projects, ...)
    event_action: str = field(default=None)  # Action performed (SignIn, SignOut, ...)
    local: bool = field(default=False)

    def __post_init__(self):
        self.event_action = type(self).__name__

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, source: dict):
        return create_class_from_required_fields(cls, source)



@dataclass
class Command:
    command_id: str = field(default_factory=uuid_id)
    command_created_date: str = field(default_factory=current_datetime_str)
    command_type: str = field(default=None)  # File name (Account, Projects, ...)
    command_action: str = field(default=None)  # Action to perform (SignIn, SignOut, ...)
    action: str = field(default="send_command")  # Route for websocket
    local: bool = field(default=False)

    def __post_init__(self):
        self.command_action = type(self).__name__

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, source: dict):
        return create_class_from_required_fields(cls, source)
