from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class FightDTO:
    name: str
    start_time: datetime
    end_time: datetime
    average_item_level: float

    encounter_id: int
    difficulty_id: int
    report_id: int | None = None

    boss_percentage: float | None = None


@dataclass
class FightListDTO:
    fights: list[FightDTO] = field(default_factory=list)


@dataclass
class EncounterDifficultyFilterDTO:
    encounter_id: int
    difficulty_id: int
