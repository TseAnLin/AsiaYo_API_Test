from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    # App settings
    usd_to_twd_rate: float = 31

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    # Get app settings (cached)
    return Settings().dict()
