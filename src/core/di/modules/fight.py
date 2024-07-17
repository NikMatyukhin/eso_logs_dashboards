import aioinject

from core.di._types import Providers
from src.domain.fight.repository import FightRepository

PROVIDERS: Providers = (aioinject.Scoped(FightRepository),)
