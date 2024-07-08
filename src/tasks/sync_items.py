import click
import inject

from src.domain.item.commands import SyncItemsCommand, SyncItemSetsCommand


@inject.params(item_sets_command=SyncItemSetsCommand, items_command=SyncItemsCommand)
def sync_items_task(
    item_sets_command: SyncItemSetsCommand, items_command: SyncItemsCommand
) -> None:
    click.echo("Running 'SyncItemSetsCommand'...")
    item_sets_command.execute()

    click.echo("Running 'SyncItemsCommand'...")
    items_command.execute()

    click.echo("Finish all tasks")
