# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .project import Project

__all__ = ["ProjectListResponse"]


class ProjectListResponse(BaseModel):
    data: List[Project]