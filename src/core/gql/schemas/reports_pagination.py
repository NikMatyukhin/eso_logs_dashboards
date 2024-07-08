from __future__ import annotations

from pydantic import BaseModel, Field


class ZoneID(BaseModel):
    id: int


class RegionID(BaseModel):
    id: int


class FightID(BaseModel):
    id: int


class ArchiveStatus(BaseModel):
    is_archived: bool = Field(..., validation_alias="isArchived")
    is_accessible: bool = Field(..., validation_alias="isAccessible")


class Report(BaseModel):
    code: str
    title: str
    start_time: int = Field(..., validation_alias="startTime")
    end_time: int = Field(..., validation_alias="endTime")
    region: RegionID | None = None
    zone: ZoneID | None = None
    fight_ids: list[FightID] | None = Field(None, validation_alias="fights")
    archive_status: ArchiveStatus = Field(..., validation_alias="archiveStatus")


class ReportsPagination(BaseModel):
    has_more_pages: bool
    reports: list[Report] = Field(..., validation_alias="data")
