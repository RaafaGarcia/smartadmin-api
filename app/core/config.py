from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "SmartAdmin API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    # Database - Railway auto-injects DATABASE_URL
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-fallback-secret-key-at-least-32-characters")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS - Permitir Railway domain
    ALLOWED_HOSTS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://*.railway.app",
        "https://*.github.io"
    ]
    
    # Railway specific
    PORT: int = int(os.getenv("PORT", 8000))
    
    class Config:
        env_file = ".env"

settings = Settings()