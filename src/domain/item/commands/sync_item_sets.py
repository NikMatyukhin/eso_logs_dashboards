import inject

from domain.item.loader import ItemLoader
from domain.item.repository import ItemRepository


class SyncItemSetsCommand:
    _item_loader: ItemLoader = inject.attr(ItemLoader)
    _item_repository: ItemRepository = inject.attr(ItemRepository)

    def execute(self) -> None:
        item_sets_list = self._item_loader.get_item_sets()
        self._item_repository.create_or_update_item_sets(item_sets_list)
