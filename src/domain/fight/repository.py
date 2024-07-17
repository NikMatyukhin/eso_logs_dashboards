from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from core.date_utils import to_datetime
from core.gql.schemas import FightInfo
from db.models import Encounter, Fight
from domain.fight.dto import EncounterDifficultyFilterDTO, FightDTO, FightListDTO


class FightRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

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
        self._session.refresh(model)

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

    def build_fight_dto(
        self,
        report_id: int,
        start_time: float,
        end_time: float,
        fights: list[FightInfo],
    ) -> FightListDTO:
        return FightListDTO(
            fights=[
                FightDTO(
                    name=fight.name,
                    start_time=to_datetime(start_time + fight.start_time),
                    end_time=to_datetime(end_time + fight.end_time),
                    average_item_level=fight.average_item_level,
                    encounter_id=fight.encounter_id,
                    difficulty_id=fight.difficulty_id,
                    report_id=report_id,
                    boss_percentage=fight.boss_percentage,
                )
                for fight in fights
                if fight.encounter_id in self.get_boss_encounters()
            ]
        )
