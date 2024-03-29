from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """
    Base settings of project.
    """
    secret_key: str
    debug: bool
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_app_settings() -> AppSettings:
    return AppSettings()
