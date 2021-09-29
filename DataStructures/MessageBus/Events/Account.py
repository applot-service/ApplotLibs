from dataclasses import dataclass
from ApplotLibs.DataStructures.MessageBus import Event
from ApplotLibs.DataStructures.User import Account
from pathlib import Path

_EVENT_TYPE = Path(__file__).stem


@dataclass
class SignedIn(Event, Account):
    event_type: str = _EVENT_TYPE


@dataclass
class NotFound(Event):
    event_type: str = _EVENT_TYPE


@dataclass
class SignedOut(Event):
    event_type: str = _EVENT_TYPE


@dataclass
class Registered(Event, Account):
    event_type: str = _EVENT_TYPE


@dataclass
class EmailAlreadyInUse(Event):
    event_type: str = _EVENT_TYPE
