import inject

from domain.ability.loader import AbilityLoader
from domain.ability.repository import AbilityRepository


class SyncAbilitiesCommand:
    _ability_loader: AbilityLoader = inject.attr(AbilityLoader)
    _ability_repository: AbilityRepository = inject.attr(AbilityRepository)

    def execute(self) -> None:
        abilities_list = self._ability_loader.get_abilities()
        self._ability_repository.create_or_update_abilities(abilities_list)
