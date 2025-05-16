"""User entity module"""

from dataclasses import dataclass
from datetime import date
from typing import Optional

from auth_service.core.domain.utils import UserRoleEnum

from .base_model import BaseModel
from .contact import Contact


@dataclass
class User(BaseModel, Contact):
    """User data class"""

    first_name: str
    last_name: str
    birthday: date
    password: str
    roles: Optional[UserRoleEnum]
