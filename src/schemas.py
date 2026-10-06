from typing import Literal

from pydantic import BaseModel, Field


class Incident(BaseModel):
    """Information available when a data pipeline incident is reported."""

    incident_id: str = Field(min_length=1)
    pipeline_name: str = Field(min_length=1)
    platform: str = Field(min_length=1)
    description: str = Field(min_length=1)
    error_message: str | None = None
    business_impact: str | None = None
    reported_priority: Literal["P1", "P2", "P3", "P4"] | None = None
