import functools
from typing import TypeVar

import dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

TSettings = TypeVar("TSettings", bound=BaseSettings)


@functools.lru_cache
def get_settings(cls: type[TSettings]) -> TSettings:
    dotenv.load_dotenv()
    return cls()


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
