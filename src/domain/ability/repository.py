from typing import Sequence

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from db.models.static import Ability
from domain.ability.dto import AbilityDTO, AbilityListDTO


class AbilityRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def create_ability(self, dto: AbilityDTO) -> Ability:
        model = Ability(
            name=dto.name,
            base_name=dto.base_name,
            icon=dto.icon,
            _type=dto._type,
        )
        self._session.add(model)
        self._session.flush()
        self._session.refresh(model)

        return model

    def create_abilities(self, dto: AbilityListDTO) -> None:
        models = [
            Ability(
                id=ability.id,
                name=ability.name,
                base_name=ability.base_name,
                icon=ability.icon,
                _type=ability._type,
            )
            for ability in dto.abilities
        ]
        self._session.add(models)
        self._session.flush()

    def create_or_update_abilities(self, dto: AbilityListDTO) -> None:
        query = insert(Ability).values(
            [
                dict(
                    id=ability.id,
                    name=ability.name,
                    base_name=ability.base_name,
                    icon=ability.icon,
                    _type=ability._type,
                )
                for ability in set(dto.abilities)
            ],
        )
        query = query.on_conflict_do_update(
            index_elements=["id"],
            set_=dict(
                name=query.excluded.name,
                base_name=query.excluded.base_name,
                icon=query.excluded.icon,
                _type=query.excluded._type,
            ),
        )
        self._session.execute(query)
        self._session.commit()

    def get_by_id(self, ability_id: int) -> Ability:
        query = select(Ability).where(Ability.id == ability_id)
        result = self._session.execute(query)
        return result.scalar_one()

    def get_by_ids(self, abilities_ids: list[int]) -> Sequence[Ability]:
        query = select(Ability).where(Ability.id.in_(abilities_ids))
        result = self._session.execute(query)
        return result.scalars().all()
