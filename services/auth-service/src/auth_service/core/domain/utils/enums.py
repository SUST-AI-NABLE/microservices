"""Enums utils"""

from enum import Enum, unique


@unique
class UserRoleEnum(str, Enum):
    """User permission enums"""

    SUPER_ADMIN = "SUPER_ADMIN"
    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"


@unique
class CountryEnum(str, Enum):
    """Country enums"""

    BJ = "BJ"
    TG = "TG"
