from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    #Configurações Gerais
    API_V1_STR: str = '/api/v1'
    DB_URL : str = 'postgresql+asyncpg://darlans:lTTb6v4ua3xy@localhost:5432/api'
    DBBaseModel = declarative_base()
    
    class Config:
        case_sensitive = True

settings = Settings()

