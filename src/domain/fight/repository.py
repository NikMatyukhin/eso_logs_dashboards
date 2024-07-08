from typing import Sequence

import inject
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models import Encounter, Fight
from domain.fight.dto import EncounterDifficultyFilterDTO, FightDTO, FightListDTO


class FightRepository:
    _session: Session = inject.attr(Session)

    def create_fight(self, dto: FightDTO) -> Fight:
        model = Fight(
            name=dto.name,
            start_time=dto.start_time,
            end_time=dto.end_time,
            average_item_level=dto.average_item_level,
            boss_percentage=dto.boss_percentage,
            report_id=dto.report_id,
            encounter_id=dto.encounter_id,
            difficulty_id=dto.difficulty_id,
        )
        self._session.add(model)
        self._session.flush()

        return model

    def create_fights(self, dto: FightListDTO) -> None:
        models = [
            Fight(
                name=fight.name,
                start_time=fight.start_time,
                end_time=fight.end_time,
                average_item_level=fight.average_item_level,
                boss_percentage=fight.boss_percentage,
                report_id=fight.report_id,
                encounter_id=fight.encounter_id,
                difficulty_id=fight.difficulty_id,
            )
            for fight in dto.fights
            if fight.encounter_id and fight.difficulty_id
        ]
        self._session.add_all(models)
        self._session.flush()

    def check_vhm_final_encounter(self, dto: EncounterDifficultyFilterDTO) -> bool:
        """
        Returns TRUE if encounter is final in trial and has veteran hard mod difficulty.
        """
        exists_criteria = (
            select(Encounter)
            .where(
                Encounter.id == dto.encounter_id,
                Encounter.vhm_difficulty_id == dto.difficulty_id,
                Encounter.is_final.is_(True),
            )
            .exists()
        )
        query = select(exists_criteria)

        return self._session.execute(query).scalar()  # type: ignore

    def get_boss_encounters(self) -> Sequence[int]:
        return self._session.execute(select(Encounter.id)).scalars().all()
