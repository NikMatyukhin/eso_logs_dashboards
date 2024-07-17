import functools
import itertools
from logging import Logger, getLogger
from typing import Iterable

import aioinject
from pydantic_settings import BaseSettings

from db.engine import create_session
from src.settings import (
    ApplicationSettings,
    AuthSettings,
    DatabaseSettings,
    LoadingSettings,
    get_settings,
)

from .modules import ability, actor, fight, item, report, spec

SETTINGS = (
    ApplicationSettings,
    AuthSettings,
    DatabaseSettings,
    LoadingSettings,
)


MODULES = (
    ability.PROVIDERS,
    actor.PROVIDERS,
    fight.PROVIDERS,
    item.PROVIDERS,
    report.PROVIDERS,
    spec.PROVIDERS,
)


def _register_settings(
    container: aioinject.Container,
    *,
    settings_classes: Iterable[type[BaseSettings]],
) -> None:
    for settings_cls in settings_classes:
        factory = functools.partial(get_settings, settings_cls)
        container.register(aioinject.Singleton(factory, type_=settings_cls))


def create_container() -> aioinject.Container:
    container = aioinject.Container()
    container.register(aioinject.Scoped(create_session))
    container.register(aioinject.Singleton(getLogger, type_=Logger))

    for provider in itertools.chain.from_iterable(MODULES):
        container.register(provider)

    _register_settings(container, settings_classes=SETTINGS)

    return container
