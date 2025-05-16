"""errors package file"""

from .base_error import BaseModelUnexpectedKeyArgumentError
from .core_exception import ICoreException

__all__ = [
    "BaseModelUnexpectedKeyArgumentError",
    "ICoreException",
]
