from dataclasses import dataclass, field
from ApplotLibs.DataStructures.MessageBus import Command
from pathlib import Path

_COMMAND_TYPE = Path(__file__).stem


@dataclass
class SignIn(Command):
    command_type: str = _COMMAND_TYPE

    email: str = field(default=None)
    password: str = field(default=None)


@dataclass
class SignOut(Command):
    command_type: str = _COMMAND_TYPE
    local: bool = True


@dataclass
class Register(Command):
    command_type: str = _COMMAND_TYPE

    first_name: str = field(default=None)
    last_name: str = field(default=None)
    company: str = field(default=None)
    email: str = field(default=None)
    password: str = field(default=None)
