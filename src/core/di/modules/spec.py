import aioinject

from core.di._types import Providers
from src.domain.spec.repository import SpecRepository

PROVIDERS: Providers = (aioinject.Scoped(SpecRepository),)
