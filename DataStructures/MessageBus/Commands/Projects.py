from dataclasses import dataclass, field
from ApplotLibs.DataStructures.MessageBus import Command
from pathlib import Path

_COMMAND_TYPE = Path(__file__).stem


@dataclass
class Pull(Command):
    command_type: str = _COMMAND_TYPE

    token: str = field(default=None)

@dataclass
class CreateProject(Command):
    command_type: str = _COMMAND_TYPE

    token: str = field(default=None)
