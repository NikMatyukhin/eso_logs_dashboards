from datetime import datetime

import click
import dotenv
from apscheduler.schedulers.background import BackgroundScheduler

from src.app import create_app
from src.core.di import configure_inject
from src.tasks import load_daily_reports_task, sync_abilities_task, sync_items_task


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option("--background", is_flag=True, show_default=True, default=False)
def start(background: bool) -> None:
    if background:
        scheduler = BackgroundScheduler()
        scheduler.add_job(load_daily_reports_task, "cron", hour="0")
        scheduler.start()
    app = create_app()
    app.run_server(debug=True)


@cli.command()
def sync_items() -> None:
    sync_items_task()


@cli.command()
def sync_abilities() -> None:
    sync_abilities_task()


@cli.command()
@click.option("--day", type=click.DateTime(formats=["%Y-%m-%d"]), default=None)
def load_reports(day: datetime | None) -> None:
    load_daily_reports_task(day=day)


if __name__ == "__main__":
    dotenv.load_dotenv(".env")
    configure_inject()
    cli()
