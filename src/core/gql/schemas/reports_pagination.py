from __future__ import annotations

from pydantic import AliasPath, BaseModel, Field, field_validator


class ZoneID(BaseModel):
    """Intermediary model, get rid of it during serialization"""

    id: int


class RegionID(BaseModel):
    """Intermediary model, get rid of it during serialization"""

    id: int


class FightID(BaseModel):
    """Intermediary model, unpack it during serialization"""

    id: int


class ArchiveStatus(BaseModel):
    """Intermediary model, get rid of it during serialization"""

    is_archived: bool = Field(..., validation_alias="isArchived")
    is_accessible: bool = Field(..., validation_alias="isAccessible")


class Report(BaseModel):
    code: str
    title: str
    start_time: int = Field(..., validation_alias="startTime")
    end_time: int = Field(..., validation_alias="endTime")
    region: int | None = Field(None, validation_alias=AliasPath("region", "id"))
    zone: int | None = Field(None, validation_alias=AliasPath("zone", "id"))
    fight_ids: list[int] = Field(..., validation_alias="fights")
    is_archived: bool = Field(
        ..., validation_alias=AliasPath("archiveStatus", "isArchived")
    )
    is_accessible: bool = Field(
        ..., validation_alias=AliasPath("archiveStatus", "isAccessible")
    )

    @field_validator("fight_ids")
    @classmethod
    def unpack_fight_ids(cls, value: list[FightID] | None) -> list[int]:
        if value is None:
            return []
        return [fight.id for fight in value]


class ReportsPagination(BaseModel):
    has_more_pages: bool
    reports: list[Report] = Field(..., validation_alias="data")
