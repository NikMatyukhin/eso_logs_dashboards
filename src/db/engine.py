from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
