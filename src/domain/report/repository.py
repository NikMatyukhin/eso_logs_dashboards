from sqlalchemy.orm import Session

from db.models import Report
from domain.report.dto import CreateReportDTO


class ReportRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def create_report(self, dto: CreateReportDTO) -> Report:
        model = Report(
            code=dto.code,
            title=dto.title,
            start_time=dto.start_time,
            end_time=dto.end_time,
            region_id=dto.region_id,
            zone_id=dto.zone_id,
            trial_time=dto.trial_time,
            trial_score=dto.trial_score,
        )
        self._session.add(model)
        self._session.flush()
        self._session.refresh(model)

        return model
