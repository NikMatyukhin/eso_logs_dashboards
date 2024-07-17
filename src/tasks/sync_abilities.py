from logging import Logger
from typing import Annotated

from aioinject import Inject, inject

from src.domain.ability.commands import SyncAbilitiesCommand


@inject
def sync_abilities_task(
    command: Annotated[SyncAbilitiesCommand, Inject],
    logger: Annotated[Logger, Inject],
) -> None:
    logger.info("Start ability synchronization task.")
    command.execute()
    logger.info("Ability synchronization task finished.")
