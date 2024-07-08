import itertools
from typing import Generator

from gql import gql

from core.gql.baseloader import GraphQLBaseLoader
from core.gql.queries import get_report_information_query, get_reports_pagination_query
from core.gql.schemas import ReportRetrieve, ReportsPagination

from .dto import LoadedReportDTO


class ReportLoader(GraphQLBaseLoader):
    """
    ReportsLoader make batches of quiries to get all reports of current day.
    """

    def _get_reports(self, start: int, end: int, page: int) -> ReportsPagination:
        pagination_query = get_reports_pagination_query(
            start_time=start, end_time=end, page=page
        )
        result = self.client.execute(gql(pagination_query.render()))

        return ReportsPagination.model_validate(
            result["reportData"]["reports"], strict=True
        )

    def _get_report(self, code: str, fight_ids: list[int]) -> ReportRetrieve:
        information_query = get_report_information_query(code=code, fight_ids=fight_ids)
        result = self.client.execute(gql(information_query.render()))

        return ReportRetrieve.model_validate(
            result["reportData"]["report"], strict=True
        )

    def process_reports(
        self, start: int, end: int
    ) -> Generator[LoadedReportDTO, object, None]:
        """
        Iterates page by page of reports for a given period. Start from 1st page.

        Skip reports:
            - without zone (most likely broken)
            - has archived status
            - has unaccessible status
        """
        for page in itertools.count(1):
            reports_page: ReportsPagination = self._get_reports(
                start=start, end=end, page=page
            )  # TODO: results + err catch
            for report in reports_page.reports:
                if report.zone is None:
                    continue
                if (
                    report.archive_status.is_archived
                    and not report.archive_status.is_accessible
                ):
                    continue

                report_info: ReportRetrieve = self._get_report(
                    code=report.code, fight_ids=[fight.id for fight in report.fight_ids]
                )  # TODO: results + err catch

                yield LoadedReportDTO(
                    code=report.code,
                    title=report.title,
                    start_time=report.start_time,
                    end_time=report.end_time,
                    region_id=report.region.id,
                    zone_id=report.zone.id,
                    fights=report_info.fights,
                    report_info=report_info.report_info,
                )
            if not reports_page.has_more_pages:
                return
