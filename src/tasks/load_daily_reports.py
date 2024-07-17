from datetime import datetime
from logging import Logger
from typing import Annotated

from aioinject import Inject, inject

from src.domain.report.commands import LoadReportCommand


@inject
def load_daily_reports_task(
    command: Annotated[LoadReportCommand, Inject],
    logger: Annotated[Logger, Inject],
    day: datetime | None = None,
) -> None:
    repr_day = (day or datetime.today()).strftime("%d.%m.%Y")
    logger.info(f"Start daily reports synchronization task for day {repr_day}.")
    command.execute(day=day)
    logger.info(f"Daily reports synchronization task finished for day {repr_day}.")
