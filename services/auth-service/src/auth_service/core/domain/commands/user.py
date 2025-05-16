"""User commands modules"""

from dataclasses import dataclass
from datetime import date
from typing import Optional

from auth_service.core.domain.utils import CountryEnum, UserRoleEnum


@dataclass
class ContactData:
    """contact data"""

    email: str
    phone_number: Optional[str]
    country: Optional[CountryEnum]


@dataclass
class CreateUserCommand:
    """create User command"""

    first_name: str
    last_name: str
    birthday: date
    contact_data: ContactData
    password: str
    roles: Optional[UserRoleEnum]
