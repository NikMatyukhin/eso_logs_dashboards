import contextlib
from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from settings import DatabaseSettings, get_settings

_settings = get_settings(DatabaseSettings)
engine = create_engine(
    _settings.url,
    pool_size=20,
    pool_pre_ping=True,
    pool_use_lifo=True,
    echo=_settings.echo,
)
session_factory = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


@contextlib.contextmanager
def create_session() -> Iterator[Session]:
    with session_factory.begin() as session:
        yield session
