"""BaseModel entity module"""

from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any, Dict
from uuid import UUID

from auth_service.core.domain.errors import BaseModelUnexpectedKeyArgumentError
from auth_service.core.domain.utils.fields import get_all_fields


@dataclass
class BaseModel:
    """BaseModel data class"""

    id_: UUID
    created_at: datetime
    update_at: datetime

    @classmethod
    def from_dict(cls, _new_obj: Dict[str, Any]) -> Any:
        """convert a dict into cls"""
        try:
            return cls(**_new_obj)

        except TypeError as e:
            unexpected_keys = set(_new_obj.keys()) - get_all_fields(cls_=cls)
            raise BaseModelUnexpectedKeyArgumentError(
                model_name=cls.__name__,
                unexpected_keys=unexpected_keys,
            ) from e

    def to_dict(self) -> Dict[str, Any]:
        """convert self to dict"""
        return asdict(self)
