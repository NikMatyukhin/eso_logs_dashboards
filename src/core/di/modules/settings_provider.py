import functools
from typing import Iterable

import inject

from settings import BaseSettings, get_settings


def register_settings(
    binder: inject.Binder,
    *,
    settings_classes: Iterable[type[BaseSettings]],
) -> None:
    for settings_cls in settings_classes:
        factory = functools.partial(get_settings, settings_cls)
        binder.bind_to_provider(settings_cls, factory)
