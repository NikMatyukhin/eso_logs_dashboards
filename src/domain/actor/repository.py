import inject
from sqlalchemy.orm import Session

from db.models.actor import Actor, ActorAbility, ActorDeathEvent, ActorItem, ActorSpec
from domain.actor.dto import (
    CreateActorAbilityDTO,
    CreateActorDeathEventDTO,
    CreateActorDTO,
    CreateActorItemDTO,
    CreateActorSpecDTO,
)


class ActorRepository:
    _session: Session = inject.attr(Session)

    def create_actor_items(self, actor_items: list[CreateActorItemDTO]) -> None:
        models = (
            ActorItem(
                actor_id=actor_item.actor_id,
                item_id=actor_item.item_id,
                trait=actor_item.trait,
                enchant=actor_item.enchant,
                slot=actor_item.slot,
            )
            for actor_item in actor_items
        )
        self._session.add_all(models)
        self._session.flush()

    def create_actor_specs(self, actor_specs: list[CreateActorSpecDTO]) -> None:
        models = (
            ActorSpec(
                actor_id=actor_spec.actor_id,
                spec_name=actor_spec.spec_name,
            )
            for actor_spec in actor_specs
        )
        self._session.add_all(models)
        self._session.flush()

    def create_actor_abilities(
        self, actor_abilities: list[CreateActorAbilityDTO]
    ) -> None:
        models = (
            ActorAbility(
                actor_id=actor_ability.actor_id,
                ability_id=actor_ability.ability_id,
            )
            for actor_ability in actor_abilities
        )
        self._session.add_all(models)
        self._session.flush()

    def create_actor_death_events(
        self, actor_death_events: list[CreateActorDeathEventDTO] | None
    ) -> None:
        if actor_death_events is None:
            return
        models = (
            ActorDeathEvent(
                actor_id=actor_death_event.actor_id,
                ability_id=actor_death_event.ability_id,
                death_time=actor_death_event.death_time,
            )
            for actor_death_event in actor_death_events
        )
        self._session.add_all(models)
        self._session.flush()

    def create_actor(self, dto: CreateActorDTO) -> Actor:
        model = Actor(
            name=dto.name,
            display_name=dto.display_name,
            damage_done=dto.damage_done,
            healing_done=dto.healing_done,
            _type=dto._type,
            sub_type=dto.sub_type,
            report_id=dto.report_id,
        )
        self._session.add(model)
        self._session.flush()

        return model

    def create_actor_info(
        self,
        items: list[CreateActorItemDTO],
        specs: list[CreateActorSpecDTO],
        abilities: list[CreateActorAbilityDTO],
        death_events: list[CreateActorDeathEventDTO] | None,
    ) -> None:
        self.create_actor_items(actor_items=items)
        self.create_actor_specs(actor_specs=specs)
        self.create_actor_abilities(actor_abilities=abilities)
        self.create_actor_death_events(actor_death_events=death_events)
