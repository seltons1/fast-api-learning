from typing import List
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = (
        "postgresql+asyncpg://darlans:lTTb6v4ua3xy@localhost:5432/api"
    )
    DBBaseModel = declarative_base()

    JWT_SECRET: str = "SrXqcTG3_3EIxVg8vHkA2E4PNe1qkxlPuRNOL3wjPGg"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()

"""
import secrets

token: str = secrets.token_urlsafe(32)
"""
