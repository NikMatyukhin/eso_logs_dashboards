from domain.item.commands import SyncItemsCommand, SyncItemSetsCommand
from domain.item.loader import ItemLoader
from domain.item.repository import ItemRepository

PROVIDERS = [
    (ItemLoader, lambda: ItemLoader()),
    (ItemRepository, lambda: ItemRepository()),
    (SyncItemsCommand, lambda: SyncItemsCommand()),
    (SyncItemSetsCommand, lambda: SyncItemSetsCommand()),
]
