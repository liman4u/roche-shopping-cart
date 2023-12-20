import os
from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Roche Shopping Cart"
    API_VERSION: str = os.getenv("API_VERSION", "0.0.1")
    API: str = "/api"
    API_V1_STR: str = "/api/v1"

    # Database
    DB_ENGINE: str = os.getenv("DB", "postgresql")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = os.getenv("DB_PORT", 5432)
    DB_USER: str = os.getenv("DB_USER", "test_db_user")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "test_pass")
    DB_NAME: str = os.getenv("DB_NAME", "test_db")

    DATABASE_URI: str = (
        "{db_engine}://{user}:{password}@{host}:{port}/{database}".format(
            db_engine=DB_ENGINE,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
        )
    )

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    # Services
    RESERVATION_SERVICE_URL: str = os.getenv(
        "RESERVATION_SERVICE_URL", "http://reservation-service:8080"
    )

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()


@lru_cache()
def get_settings():
    return settings
