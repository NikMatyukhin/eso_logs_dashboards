from typing import TypeVar

_T = TypeVar("_T")


def getval(value: _T | None, default: _T) -> _T:
    if value is None:
        return default
    return value
