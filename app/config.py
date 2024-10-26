import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

def get_config() -> Settings:
    return Settings()
