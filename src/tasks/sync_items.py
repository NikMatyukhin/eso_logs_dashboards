from logging import Logger
from typing import Annotated

from aioinject import Inject, inject

from src.domain.item.commands import SyncItemsCommand, SyncItemSetsCommand


@inject
def sync_items_task(
    item_sets_command: Annotated[SyncItemSetsCommand, Inject],
    items_command: Annotated[SyncItemsCommand, Inject],
    logger: Annotated[Logger, Inject],
) -> None:
    logger.info("Start item sets syncronization task.")
    item_sets_command.execute()
    logger.info("Item sets syncronization task finished.")

    logger.info("Start items syncronization task.")
    items_command.execute()
    logger.info("Items syncronization task finished.")
