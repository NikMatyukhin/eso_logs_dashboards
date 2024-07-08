from graphql_query import Argument, Field, Operation, Query


def get_reports_pagination_query(
    start_time: int,
    end_time: int,
    page: int,
) -> Operation:
    report_data = Query(
        name="reportData",
        fields=[
            Field(
                name="reports",
                arguments=[
                    Argument(name="startTime", value=start_time),
                    Argument(name="endTime", value=end_time),
                    Argument(name="page", value=page),
                ],
                fields=[
                    "has_more_pages",
                    Field(
                        name="data",
                        fields=[
                            "title",
                            "code",
                            "startTime",
                            "endTime",
                            Field(name="zone", fields=["id"]),
                            Field(name="region", fields=["id"]),
                            Field(name="fights", fields=["id"]),
                            Field(
                                name="archiveStatus",
                                fields=["isArchived", "isAccessible"],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )

    return Operation(type="query", queries=[report_data])
