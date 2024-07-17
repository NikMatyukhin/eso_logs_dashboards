from domain.item.loader import ItemLoader
from domain.item.repository import ItemRepository


class SyncItemsCommand:
    def __init__(
        self,
        item_loader: ItemLoader,
        item_repository: ItemRepository,
    ) -> None:
        self._item_loader = item_loader
        self._item_repository = item_repository

    def execute(self) -> None:
        for items_list in self._item_loader.get_items():
            self._item_repository.create_or_update_items(items_list)


class SyncItemSetsCommand:
    def __init__(
        self,
        item_loader: ItemLoader,
        item_repository: ItemRepository,
    ) -> None:
        self._item_loader = item_loader
        self._item_repository = item_repository

    def execute(self) -> None:
        item_sets_list = self._item_loader.get_item_sets()
        self._item_repository.create_or_update_item_sets(item_sets_list)
