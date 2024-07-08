from typing import Mapping

import inject

from core.gql.schemas import (
    CompositionItem,
    DeathEvent,
    HealthChangeItem,
    Player,
    PlayerDetails,
)
from core.transform_utils import transform_to_id_map, transform_to_id_seq_map
from db.models.report import Report
from domain.actor.dto import (
    CreateActorAbilityDTO,
    CreateActorDeathEventDTO,
    CreateActorDTO,
    CreateActorItemDTO,
    CreateActorSpecDTO,
)
from domain.actor.repository import ActorRepository


class ActorService:
    _actor_repository: ActorRepository = inject.attr(ActorRepository)

    def create_report_actors(
        self,
        report: Report,
        composition_list: list[CompositionItem],
        damage_done_list: list[HealthChangeItem],
        healing_done_list: list[HealthChangeItem],
        death_event_list: list[DeathEvent],
        player_details: PlayerDetails,
    ) -> None:
        composition_id_map = transform_to_id_map(composition_list)
        damage_done_id_map = transform_to_id_map(damage_done_list)
        healing_done_id_map = transform_to_id_map(healing_done_list)
        death_events_id_map = transform_to_id_seq_map(death_event_list)

        tanks_id_map = transform_to_id_map(player_details.tanks)
        healers_id_map = transform_to_id_map(player_details.healers)
        damage_dealers_id_map = transform_to_id_map(player_details.dps)

        player_details_id_map: Mapping[int, Player] = (
            damage_dealers_id_map | healers_id_map | tanks_id_map
        )

        for _id in composition_id_map:
            if _id not in player_details:
                continue
            actor_dto = CreateActorDTO(
                name=composition_id_map[_id].name,
                display_name=player_details_id_map[_id].display_name,
                damage_done=damage_done_id_map[_id].total,
                healing_done=healing_done_id_map[_id].total,
                _type=composition_id_map[_id].type,
                sub_type=player_details_id_map[_id].icon,
                report_id=report.id,
            )
            actor = self._actor_repository.create_actor(dto=actor_dto)
            specs = [
                CreateActorSpecDTO(
                    spec_name=spec,
                    actor_id=actor.id,
                )
                for spec in player_details_id_map[_id].specs
            ]
            items = []
            abilities = []
            if not isinstance(player_details_id_map[_id].combatant_info, list):
                items = [
                    CreateActorItemDTO(
                        item_id=gear.id,
                        actor_id=actor.id,
                        trait=gear.trait,
                        enchant=gear.enchant_type,
                        slot=gear.slot,
                    )
                    for gear in player_details_id_map[_id].combatant_info.gear
                    if gear.id
                ]
                abilities = [
                    CreateActorAbilityDTO(
                        ability_id=talent.guid,
                        actor_id=actor.id,
                    )
                    for talent in player_details_id_map[_id].combatant_info.talents
                    if talent.guid
                ]
            death_events = (
                [
                    CreateActorDeathEventDTO(
                        death_time=death_event.death_time,
                        ability_id=death_event.ability.guid,
                        actor_id=actor.id,
                    )
                    for death_event in death_events_id_map[_id]
                ]
                if death_events_id_map
                else None
            )
            self._actor_repository.create_actor_info(
                items=items, specs=specs, abilities=abilities, death_events=death_events
            )
