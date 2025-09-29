# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, Dict

from .._models import BaseModel

__all__ = ["ToolListItem"]


class ToolListItem(BaseModel):
    id: str

    description: str

    parameters: Dict[str, Any]