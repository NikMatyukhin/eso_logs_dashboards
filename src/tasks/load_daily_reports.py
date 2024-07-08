from datetime import datetime

import click
import inject

from src.domain.report.commands import LoadReportCommand


@inject.params(command=LoadReportCommand)
def load_daily_reports_task(
    command: LoadReportCommand, day: datetime | None = None
) -> None:
    click.echo(f"Start load report for {day or 'today'} day:")
    click.echo("Running 'LoadReportCommand'...")

    command.execute(day=day)

    click.echo("Finish all tasks")
