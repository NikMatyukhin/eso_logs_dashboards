from src.domain.ability.loader import AbilityLoader
from src.domain.ability.repository import AbilityRepository


class SyncAbilitiesCommand:
    def __init__(
        self,
        ability_loader: AbilityLoader,
        ability_repository: AbilityRepository,
    ) -> None:
        self._ability_loader = ability_loader
        self._ability_repository = ability_repository

    def execute(self) -> None:
        abilities_list = self._ability_loader.get_abilities()
        self._ability_repository.create_or_update_abilities(abilities_list)
