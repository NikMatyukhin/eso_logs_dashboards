from __future__ import annotations

from pydantic import AliasPath, BaseModel, Field, field_validator


class BaseModelWithID(BaseModel):
    """Transform annotation class with required `id` attribute"""
    id: int


class FightInfo(BaseModel):
    name: str
    kill: bool | None = None
    encounter_id: int = Field(..., validation_alias="encounterID")
    start_time: int = Field(..., validation_alias="startTime")
    end_time: int = Field(..., validation_alias="endTime")
    average_item_level: float = Field(..., validation_alias="averageItemLevel")
    trial_score: int | None = Field(None, validation_alias="trialScore")
    trial_time: int | None = Field(None, validation_alias="trialTime")
    difficulty_id: int | None = Field(None, validation_alias="difficulty")
    boss_percentage: float | None = Field(None, validation_alias="bossPercentage")


class Spec(BaseModel):
    spec: str
    role: str


class CompositionItem(BaseModelWithID):
    name: str
    guid: int
    type: str
    specs: list[Spec]


class HealthChangeItem(BaseModelWithID):
    name: str
    guid: int
    type: str
    icon: str
    total: int


class DamageTakenItem(BaseModel):
    guid: int
    name: str
    type: int
    total: int
    flags: int | None = None
    composite: bool | None = None
    ability_icon: str = Field(..., validation_alias="abilityIcon")


class Ability(BaseModel):
    guid: int
    name: str
    type: int
    flags: int
    ability_icon: str = Field(..., validation_alias="abilityIcon")


class DeathEvent(BaseModelWithID):
    name: str
    guid: int
    type: str
    icon: str
    death_time: int = Field(..., validation_alias="deathTime")
    ability: Ability | None = None


class GearItem(BaseModelWithID):
    icon: str
    slot: int
    trait: int
    quality: int
    type: int | None = None
    name: str | None = None
    champion_points: int = Field(..., validation_alias="championPoints")
    enchant_type: int = Field(..., validation_alias="enchantType")
    enchant_quality: int = Field(..., validation_alias="enchantQuality")
    set_id: int = Field(..., validation_alias="setID")
    set_name: str | None = Field(None, validation_alias="setName")


class CombatantInfo(BaseModel):
    stats: list[object]
    talents: list[Ability] | None = None
    gear: list[GearItem] | None = None


class Player(BaseModelWithID):
    icon: str
    name: str
    guid: int
    type: str
    server: str
    anonymous: bool
    specs: list[str]
    display_name: str = Field(..., validation_alias="displayName")
    min_item_level: int | None = Field(None, validation_alias="minItemLevel")
    max_item_level: int | None = Field(None, validation_alias="maxItemLevel")
    potion_use: int = Field(..., validation_alias="potionUse")
    healthstone_use: int = Field(..., validation_alias="healthstoneUse")
    combatant_info: CombatantInfo | None = Field(None, validation_alias="combatantInfo")

    @field_validator("combatant_info")
    @classmethod
    def list_value_to_none(
        cls, value: CombatantInfo | list[object] | None
    ) -> CombatantInfo | None:
        if isinstance(value, CombatantInfo):
            return value
        return None


class PlayerDetails(BaseModel):
    healers: list[Player] | None = None
    tanks: list[Player] | None = None
    dps: list[Player] | None = None


class ReportInfo(BaseModel):
    total_time: int = Field(..., validation_alias="totalTime")
    item_level: float = Field(..., validation_alias="itemLevel")
    composition: list[CompositionItem]
    damage_done: list[HealthChangeItem] = Field(..., validation_alias="damageDone")
    healing_done: list[HealthChangeItem] = Field(..., validation_alias="healingDone")
    damage_taken: list[DamageTakenItem] = Field(..., validation_alias="damageTaken")
    death_events: list[DeathEvent] = Field(..., validation_alias="deathEvents")
    player_details: PlayerDetails = Field(..., validation_alias="playerDetails")
    log_version: int = Field(..., validation_alias="logVersion")
    game_version: int = Field(..., validation_alias="gameVersion")


class Details(BaseModel):
    """Intermediary model, get rid of it during serialization"""

    data: ReportInfo


class ReportRetrieve(BaseModel):
    report_info: ReportInfo | None = Field(
        None, validation_alias=AliasPath("table", "data")
    )
    fights: list[FightInfo] | None = None
    trial_score: int | None = Field(None, validation_alias="trialScore")
    trial_time: int | None = Field(None, validation_alias="trialTime")
