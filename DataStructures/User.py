from dataclasses import dataclass, field
from ApplotLibs.Utilities.helpers import uuid_id, current_datetime_str

from typing import List


@dataclass
class ProjectID:
    project_id: str = field(default=None)


@dataclass
class Account:
    account_id: str = field(default_factory=uuid_id)
    entity_created_date: str = field(default_factory=current_datetime_str)
    first_name: str = field(default=None)
    last_name: str = field(default=None)
    company: str = field(default=None)
    email: str = field(default=None)
    token: str = field(default=None)
    password: str = field(default=None)
    projects: List[ProjectID] = field(default=None)
