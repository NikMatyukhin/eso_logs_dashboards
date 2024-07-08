from datetime import datetime, time, timedelta

import pytz

FACTOR = 1000


def get_day_time_interval(day: datetime | None = None) -> tuple[int, int]:
    """
    Create a pair of integers's for the start & end of the day. If еру day isn't provided - use today's date.

    https://currentmillis.com/#python
    """
    today = day or datetime.today() - timedelta(days=1)
    start_of_today = datetime.combine(
        today,
        time(0, 0, 0),
        tzinfo=pytz.utc,
    )
    end_of_today = datetime.combine(
        today + timedelta(days=1),
        time(0, 0, 0),
        tzinfo=pytz.utc,
    )
    return int(start_of_today.timestamp()) * FACTOR, int(
        end_of_today.timestamp()
    ) * FACTOR


def to_datetime(epoch_time: int | float) -> datetime:
    """
    Convert milliseconds since epoch to `datetime.datetime` object.

    https://currentmillis.com/#python
    """
    return datetime.fromtimestamp(epoch_time / FACTOR)
