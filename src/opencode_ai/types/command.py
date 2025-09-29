# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._types import BaseModel

__all__ = ["Command"]


class Command(BaseModel):
    id: str
    name: str
    description: str