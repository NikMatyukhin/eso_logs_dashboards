from domain.ability.loader import AbilityLoader
from domain.ability.repository import AbilityRepository

PROVIDERS = [
    (AbilityLoader, lambda: AbilityLoader()),
    (AbilityRepository, lambda: AbilityRepository()),
]
