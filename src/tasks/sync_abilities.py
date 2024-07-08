import click
import inject

from src.domain.ability.commands import SyncAbilitiesCommand


@inject.params(command=SyncAbilitiesCommand)
def sync_abilities_task(command: SyncAbilitiesCommand) -> None:
    click.echo("Running 'SyncAbilitiesCommand'...")
    command.execute()

    click.echo("Finish all tasks")
