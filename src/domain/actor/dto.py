from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class CreateActorDTO:
    name: str
    display_name: str
    damage_done: int
    healing_done: int
    _type: str
    sub_type: str

    report_id: UUID


@dataclass
class CreateActorItemDTO:
    actor_id: UUID
    item_id: int
    trait: int
    enchant: int
    slot: int


@dataclass
class CreateActorSpecDTO:
    actor_id: UUID
    spec_name: str


@dataclass
class CreateActorAbilityDTO:
    actor_id: UUID
    ability_id: int


@dataclass
class CreateActorDeathEventDTO:
    death_time: datetime
    ability_id: int
    actor_id: UUID
