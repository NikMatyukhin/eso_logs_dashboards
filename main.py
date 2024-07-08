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


@click.command()
def start() -> None:
    dotenv.load_dotenv(".env")
    scheduler = BackgroundScheduler()
    scheduler.add_job(load_daily_reports_task, "cron", hour="0")
    scheduler.start()
    app = create_app()
    app.run_server(debug=True)


@click.command()
def sync_items() -> None:
    dotenv.load_dotenv(".env")
    sync_items_task()


@click.command()
def sync_abilities() -> None:
    dotenv.load_dotenv(".env")
    sync_abilities_task()


@click.command()
@click.option("--day", type=click.DateTime(formats=["%Y-%m-%d"]), default=None)
def load_reports(day: datetime | None) -> None:
    dotenv.load_dotenv(".env")
    load_daily_reports_task(day=day)


if __name__ == "__main__":
    configure_inject()

    cli.add_command(start)
    cli.add_command(sync_items)
    cli.add_command(sync_abilities)
    cli.add_command(load_reports)

    cli()
