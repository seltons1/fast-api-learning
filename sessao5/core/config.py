from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://darlans:lTTb6v4ua3xy@localhost:5432/apiSQLModel'

    class Config:
        case_sensitive = True


settings = Settings()
