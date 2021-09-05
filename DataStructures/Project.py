from dataclasses import dataclass, field
from ApplotLibs.Utilities.helpers import uuid_id, current_datetime_str
from ApplotLibs.DataStructures import Policies

from typing import List, Dict


class ProjectNotFound(Exception):
    pass


@dataclass
class Resource:
    object_name: str = field(default=None)
    is_used: bool = field(default=False)
    description: str = field(default=None)


@dataclass
class VersionsControl:
    pass


@dataclass
class AccountWithPolicies:
    account_id: str = field(default=None)
    project: Policies.Project = field(default=None)
    pages: Policies.Pages = field(default=None)
    items: Policies.Items = field(default=None)
    media: Policies.Media = field(default=None)
    users: Policies.Users = field(default=None)


@dataclass
class BaseProject:
    project_id: str = field(default_factory=uuid_id)
    title: str = field(default="Project title")
    description: str = field(default="This is project description...")
    last_updated: str = field(default=None)
    entity_created_date: str = field(default_factory=current_datetime_str)
    resources: Dict[str, Resource] = field(default={})
    versions_control: VersionsControl = field(default=None)
    participants: Dict[str, AccountWithPolicies] = field(default={})
