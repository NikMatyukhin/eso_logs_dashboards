from graphql_query import Argument, Field, Operation, Query


def get_report_information_query(
    code: str,
    fight_ids: list[int],
) -> Operation:
    report = Query(
        name="reportData",
        fields=[
            Field(
                name="report",
                arguments=[Argument(name="code", value=f'"{code}"')],
                fields=[
                    Field(
                        name="table",
                        arguments=[Argument(name="fightIDs", value=fight_ids)],
                    ),
                    Field(
                        name="playerDetails",
                        arguments=[Argument(name="fightIDs", value=fight_ids)],
                    ),
                    Field(
                        name="fights",
                        fields=[
                            "id",
                            "encounterID",
                            "name",
                            "kill",
                            "startTime",
                            "endTime",
                            "trialScore",
                            "trialTime",
                            "averageItemLevel",
                            "difficulty",
                            "bossPercentage",
                        ],
                    ),
                ],
            ),
        ],
    )

    return Operation(type="query", queries=[report])


def get_report_base_query(
    code: str,
) -> Operation:
    report = Query(
        name="reportData",
        fields=[
            Field(
                name="report",
                arguments=[Argument(name="code", value=f'"{code}"')],
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
    )

    return Operation(type="query", queries=[report])
