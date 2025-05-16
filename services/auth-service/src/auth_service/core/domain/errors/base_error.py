"""base errors module."""

from typing import Set

from .core_exception import ICoreException


class BaseModelUnexpectedKeyArgumentError(ICoreException):
    """Error thrown when a BaseModel is initialized with unexpected key arguments."""

    def __init__(self, model_name: str, unexpected_keys: Set[str]):
        self.message = f"Unexpected keys in {
            model_name} initialization: {', '.join(unexpected_keys)}"
        self.http_code = 422
        self.key = "baseModelUnexpectedKeyArgumentError"
        super().__init__()
