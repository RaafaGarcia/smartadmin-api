import os
from typing import List
from pydantic import BaseModel

class Settings(BaseModel):
    PROJECT_NAME: str = "SmartAdmin API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    # Database - Render auto-injects DATABASE_URL
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    
    # Security
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY", 
        "smartadmin-fallback-secret-key-change-in-production-32-chars"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS - Include Render domains
    ALLOWED_HOSTS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://*.onrender.com",
        "https://*.github.io",
        "https://smartadmin-api.onrender.com"  # Tu dominio específico
    ]
    
    # Render specific
    PORT: int = int(os.getenv("PORT", 8000))
    RENDER_EXTERNAL_URL: str = os.getenv("RENDER_EXTERNAL_URL", "")

# Create settings instance
settings = Settings()