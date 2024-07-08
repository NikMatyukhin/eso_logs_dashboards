import inject

from domain.item.loader import ItemLoader
from domain.item.repository import ItemRepository


class SyncItemsCommand:
    _item_loader: ItemLoader = inject.attr(ItemLoader)
    _item_repository: ItemRepository = inject.attr(ItemRepository)

    def execute(self) -> None:
        for items_list in self._item_loader.get_items():
            self._item_repository.create_or_update_items(items_list)
