from gql import gql
from graphql_query import Argument, Field, Operation, Query

from src.auth import AuthenticatedFetcher

from .schemas import ReportData


class ReportsFetcher(AuthenticatedFetcher):

    def _get_reports_operation(self) -> Operation:
        report_data = Query(
            name="reportData",
            fields=[
                Field(
                    name="reports",
                    arguments=[
                        Argument(name="startTime", value=1717088400000),
                        Argument(name="endTime", value=1717174799000),
                        Argument(name="page", value=1),
                    ],
                    fields=[
                        "has_more_pages",
                        Field(
                            name="data",
                            fields=[
                                "code",
                                "visibility",
                                Field(name="zone", fields=["name"]),
                            ],
                        ),
                    ],
                ),
            ],
        )

        return Operation(type="query", queries=[report_data])

    def execute(self) -> ReportData:
        query = gql(self._get_reports_operation().render())

        result = self.client.execute(query)

        return ReportData.model_validate(result["reportData"], strict=True)
