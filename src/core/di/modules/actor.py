import aioinject

from core.di._types import Providers
from src.domain.actor.repository import ActorRepository
from src.domain.actor.service import ActorService

PROVIDERS: Providers = (
    aioinject.Scoped(ActorRepository),
    aioinject.Scoped(ActorService),
)
