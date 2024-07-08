import itertools

import inject
from sqlalchemy.orm import Session

from db.engine import create_session
from settings import ApplicationSettings, AuthSettings, DatabaseSettings

from .modules import abilities, actors, fights, items, reports, settings_provider, specs

PROVIDERS = [
    abilities.PROVIDERS,
    actors.PROVIDERS,
    items.PROVIDERS,
    fights.PROVIDERS,
    reports.PROVIDERS,
    specs.PROVIDERS,
]


SETTINGS = (
    ApplicationSettings,
    AuthSettings,
    DatabaseSettings,
)


def base_configuration(binder: inject.Binder) -> None:
    """
    Configurator described by `inject.BinderCallable` signature from python-inject `Callable[[inject.Binder], None]`
    """
    binder.bind_to_provider(Session, create_session)

    for provided_class, provider in itertools.chain.from_iterable(PROVIDERS):
        binder.bind_to_provider(cls=provided_class, provider=provider)

    settings_provider.register_settings(binder=binder, settings_classes=SETTINGS)


def configure_inject() -> None:
    inject.configure(
        base_configuration, bind_in_runtime=True, allow_override=True, once=True
    )
