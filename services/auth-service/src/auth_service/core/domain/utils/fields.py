"""retrieve object fields module"""

from typing import Set, TypeVar

MODELTYPE = TypeVar("MODELTYPE")


def get_all_fields(cls_: MODELTYPE) -> Set[str]:
    """Get all fields of the dataclass"""
    fields = list(cls_.__annotations__.keys())
    for _cls in cls_.__bases__:
        fields.extend(list(_cls.__annotations__.keys()))

    return set(fields)
