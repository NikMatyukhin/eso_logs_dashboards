import math
from datetime import datetime
from typing import Iterator

import more_itertools

from core.date_utils import get_day_time_interval, to_datetime
from core.gql.schemas import FightInfo
from core.null_safety import getval
from domain.actor.service import ActorService
from domain.fight.dto import EncounterDifficultyFilterDTO
from domain.fight.repository import FightRepository
from domain.report.dto import CreateReportDTO
from domain.report.loader import ReportLoader
from domain.report.repository import ReportRepository


class LoadReportCommand:
    def __init__(
        self,
        report_loader: ReportLoader,
        report_repository: ReportRepository,
        fight_repository: FightRepository,
        actor_service: ActorService,
    ) -> None:
        self._report_loader = report_loader
        self._report_repository = report_repository
        self._fight_repository = fight_repository
        self._actor_service = actor_service

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

    def _split_by_reruns(
        self, fights: list[FightInfo]
    ) -> Iterator[tuple[list[FightInfo], ...]]:
        return more_itertools.grouper(
            iterable=more_itertools.split_at(
                iterable=fights,
                pred=self._is_encounter_final_fight_vhm,
                keep_separator=True,
            ),
            n=2,
            incomplete="ignore",
        )

    def execute(self, day: datetime | None = None) -> None:
        """
        Loading all reports for choosen day (current day by default)
        """
        start, end = get_day_time_interval(day=day)

        for loaded_report in self._report_loader.process_reports(start=start, end=end):
            # Iterate by pagination responses under the hood
            report_reruns = self._split_by_reruns(loaded_report.fights)

            for base_fights_list, final_fight_list in report_reruns:
                # fights of trial, final_fight always list with 1 element
                fights = base_fights_list + final_fight_list

                report = self._report_repository.create_report(
                    dto=CreateReportDTO(
                        code=loaded_report.code,
                        title=loaded_report.title,
                        start_time=to_datetime(loaded_report.start_time),
                        end_time=to_datetime(loaded_report.end_time),
                        region_id=loaded_report.region_id,
                        zone_id=loaded_report.zone_id,
                        trial_score=getval(fights[-1].trial_score, 0),
                        trial_time=to_datetime(
                            loaded_report.start_time + getval(fights[-1].trial_time, 0)
                        ),
                    )
                )
                self._fight_repository.create_fights(
                    dto=self._fight_repository.build_fight_dto(
                        report_id=report.id,
                        start_time=loaded_report.start_time,
                        end_time=loaded_report.end_time,
                        fights=fights,
                    )
                )
                self._actor_service.create_report_actors(
                    report=report,
                    composition_list=loaded_report.report_info.details.composition,
                    damage_done_list=loaded_report.report_info.details.damage_done,
                    healing_done_list=loaded_report.report_info.details.healing_done,
                    player_details=loaded_report.report_info.details.player_details,
                    death_event_list=loaded_report.report_info.details.death_events,
                )
