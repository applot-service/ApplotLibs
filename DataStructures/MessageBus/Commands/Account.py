from dataclasses import dataclass, field
from ApplotLibs.DataStructures.MessageBus import Command


@dataclass
class SignIn(Command):
    email: str = field(default=None)
    password: str = field(default=None)
    command: str = field(default="account. sign in")


@dataclass
class SignOut(Command):
    command: str = field(default="account. sign out")


@dataclass
class Register(Command):
    first_name: str = field(default=None)
    last_name: str = field(default=None)
    company: str = field(default=None)
    email: str = field(default=None)
    password: str = field(default=None)
    command: str = field(default="account. register")
