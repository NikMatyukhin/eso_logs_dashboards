import logging
from datetime import datetime

import click
from apscheduler.schedulers.background import BackgroundScheduler

from src.app import create_app
from src.core.di import create_container
from src.tasks import load_daily_reports_task, sync_abilities_task, sync_items_task


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option("--background", is_flag=True, show_default=True, default=False)
def start(background: bool) -> None:
    container = create_container()
    with container.sync_context():
        if background:
            scheduler = BackgroundScheduler()
            scheduler.add_job(load_daily_reports_task, "cron", hour="0")
            scheduler.start()
    app = create_app()
    app.run_server(debug=True)


@cli.command()
def sync_items() -> None:
    container = create_container()
    with container.sync_context():
        sync_items_task()  # type: ignore


@cli.command()
def sync_abilities() -> None:
    container = create_container()
    with container.sync_context():
        sync_abilities_task()  # type: ignore


@cli.command()
@click.option("--day", type=click.DateTime(formats=["%Y-%m-%d"]), default=None)
def load_reports(day: datetime | None) -> None:
    container = create_container()
    with container.sync_context():
        load_daily_reports_task(day=day)  # type: ignore


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    cli()
