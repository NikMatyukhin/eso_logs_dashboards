import functools
from typing import TypeVar

import dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

TSettings = TypeVar("TSettings", bound=BaseSettings)


def get_settings(cls: type[TSettings]) -> TSettings:
    dotenv.load_dotenv()
    return cls()


get_settings = functools.lru_cache(get_settings)  # mypy moment


class ApplicationSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="app_")

    client_endpoint_url: str


class AuthSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="auth_")

    client_id: str
    client_secret: str
    grant_type: str

    oauth_token_url: str

    token_header: str
    token_type: str


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="database_")

    driver: str = "postgresql+psycopg2"
    name: str
    username: str
    password: str
    host: str

    echo: bool = False

    @property
    def url(self) -> str:
        return (
            f"{self.driver}://{self.username}:{self.password}@{self.host}/{self.name}"
        )


class LoadingSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="loading_")

    abilities_url: str
    items_url: str
    item_sets_url: str
