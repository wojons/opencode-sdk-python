# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._types import BaseModel

__all__ = ["CommandListResponse"]


class CommandListResponse(BaseModel):
    commands: List["Command"]