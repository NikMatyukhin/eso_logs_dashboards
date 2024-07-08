import math
from datetime import datetime

import click
import inject
import more_itertools
from sqlalchemy.orm import Session

from core.date_utils import get_day_time_interval, to_datetime
from core.gql.schemas import FightInfo
from domain.actor.service import ActorService
from domain.fight.dto import EncounterDifficultyFilterDTO, FightDTO, FightListDTO
from domain.fight.repository import FightRepository
from domain.report.dto import CreateReportDTO
from domain.report.loader import ReportLoader
from domain.report.repository import ReportRepository


class LoadReportCommand:
    _session: Session = inject.attr(Session)
    _report_loader: ReportLoader = inject.attr(ReportLoader)
    _report_repository: ReportRepository = inject.attr(ReportRepository)
    _fight_repository: FightRepository = inject.attr(FightRepository)
    _actor_service: ActorService = inject.attr(ActorService)

    def __init__(self) -> None:
        self._encounters = set(self._fight_repository.get_boss_encounters())

    def _build_fight_dto(
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
                if fight.encounter_id in self._encounters
            ]
        )

    def _is_encounter_final_fight_vhm(self, fight: FightInfo) -> bool:
        filters = EncounterDifficultyFilterDTO(
            encounter_id=fight.encounter_id,
            difficulty_id=fight.difficulty_id,
        )
        if not self._fight_repository.check_vhm_final_encounter(filters):
            return False
        if fight.trial_time is None or fight.trial_score is None:
            return fight.boss_percentage is not None and math.isclose(
                fight.boss_percentage, 0.01
            )
        return True

    def execute(self, day: datetime | None = None) -> None:
        start, end = get_day_time_interval(day=day)
        click.echo(f"Loading reports from {start} to {end}")
        for loaded_report in self._report_loader.process_reports(start=start, end=end):
            click.echo(
                f"Creating report '{loaded_report.code}' - '{loaded_report.title}'"
            )
            report_reruns = more_itertools.grouper(
                iterable=more_itertools.split_at(
                    iterable=loaded_report.fights,
                    pred=self._is_encounter_final_fight_vhm,
                    keep_separator=True,
                ),
                n=2,
                incomplete="ignore",
            )
            for base_fights_list, final_fight_list in report_reruns:
                fights = base_fights_list + final_fight_list
                create_report_dto = CreateReportDTO(
                    code=loaded_report.code,
                    title=loaded_report.title,
                    start_time=to_datetime(loaded_report.start_time),
                    end_time=to_datetime(loaded_report.end_time),
                    region_id=loaded_report.region_id,
                    zone_id=loaded_report.zone_id,
                    trial_score=fights[-1].trial_score,
                    trial_time=to_datetime(
                        loaded_report.start_time + fights[-1].trial_time
                    ),
                )
                report = self._report_repository.create_report(dto=create_report_dto)
                fight_list_dto = self._build_fight_dto(
                    report_id=report.id,
                    start_time=loaded_report.start_time,
                    end_time=loaded_report.end_time,
                    fights=fights,
                )
                self._fight_repository.create_fights(dto=fight_list_dto)
                self._actor_service.create_report_actors(
                    report=report,
                    composition_list=loaded_report.report_info.details.composition,
                    damage_done_list=loaded_report.report_info.details.damage_done,
                    healing_done_list=loaded_report.report_info.details.healing_done,
                    player_details=loaded_report.report_info.details.player_details,
                    death_event_list=loaded_report.report_info.details.death_events,
                )
                self._session.commit()
                self._session.flush()
