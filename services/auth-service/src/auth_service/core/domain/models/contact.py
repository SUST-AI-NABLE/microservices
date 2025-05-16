"""Contact entity module"""

from dataclasses import dataclass
from typing import Optional

from auth_service.core.domain.utils import CountryEnum


@dataclass
class Contact:
    """Contact data class"""

    email: str
    phone_number: Optional[str]
    country: Optional[CountryEnum]
