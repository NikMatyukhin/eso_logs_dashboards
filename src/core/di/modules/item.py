import aioinject

from core.di._types import Providers
from src.domain.item.commands import SyncItemsCommand, SyncItemSetsCommand
from src.domain.item.loader import ItemLoader
from src.domain.item.repository import ItemRepository

PROVIDERS: Providers = (
    aioinject.Scoped(ItemRepository),
    aioinject.Scoped(ItemLoader),
    aioinject.Scoped(SyncItemsCommand),
    aioinject.Scoped(SyncItemSetsCommand),
)
