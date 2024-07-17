import aioinject

from core.di._types import Providers
from src.domain.ability.commands import SyncAbilitiesCommand
from src.domain.ability.loader import AbilityLoader
from src.domain.ability.repository import AbilityRepository

PROVIDERS: Providers = (
    aioinject.Scoped(AbilityRepository),
    aioinject.Scoped(AbilityLoader),
    aioinject.Scoped(SyncAbilitiesCommand),
)
