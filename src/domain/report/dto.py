from dataclasses import dataclass
from datetime import datetime

from core.gql.schemas import FightInfo, ReportInfo


@dataclass
class _BaseReportDTO:
    code: str
    title: str

    region_id: int
    zone_id: int


@dataclass
class CreateReportDTO(_BaseReportDTO):
    trial_time: datetime
    trial_score: int
    start_time: datetime
    end_time: datetime


@dataclass
class LoadedReportDTO(_BaseReportDTO):
    fights: list[FightInfo]
    report_info: ReportInfo
    start_time: int
    end_time: int
