"""core exception module"""

from fastapi import HTTPException


class ICoreException(HTTPException):
    """Base class for all core exceptions."""

    message: str
    http_code: int
    key: str

    def __init__(self):
        super().__init__(
            status_code=self.http_code,
            detail=f"{self.message} ({self.key})",
        )

    def __str__(self):
        return f"[{self.key}] {self.message}"
