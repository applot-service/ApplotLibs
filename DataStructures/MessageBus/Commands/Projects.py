from dataclasses import dataclass, field
from ApplotLibs.DataStructures.MessageBus import Command


@dataclass
class Pull(Command):
    token: str = field(default=None)
    command = "projects. pull"

@dataclass
class CreateProject(Command):
    token: str = field(default=None)
    command = "projects. create project"
