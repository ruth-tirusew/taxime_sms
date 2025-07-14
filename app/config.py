from pydantic_settings import BaseSettings
from typing import Optional,Any

class Settings(BaseSettings):
    CORS_ORIGINS: list[str] = ["*"]
    CORS_HEADERS: list[str] = ["*"]
    CORS_METHODS: list[str] = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]

    SMS_PROVIDER: str = "afrosms"
    SENDER_NAME: str = 'taxime'
    
    # Afrosms
    AFROSMS_URL:str="https://api.afromessage.com"
    AFROSMS_IDENTIFIER_URL:Optional[str]=None
    AFROSMS_TOKEN:Optional[str]=None


    # TELE configs

 
    DATABASE_URL: str = "sqlite:///./test.db"
    
    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    return Settings()

settings = get_settings()

fastapi_config: dict[str, Any] = {
    "title": "Taxime sms",
}