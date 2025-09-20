from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "SmartAdmin API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    # Database - Render auto-injects DATABASE_URL
    DATABASE_URL: str = "sqlite:///./test.db"
    
    # Security
    SECRET_KEY: str = "smartadmin-fallback-secret-key-change-in-production-32-chars"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS - Include Render domains
    ALLOWED_HOSTS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://raafagarcia.github.io",          # tu frontend en GitHub Pages
        "https://smartadmin-api.onrender.com",
        "https://*.onrender.com"  
    ]
    
    # Render specific
    PORT: int = 8000
    RENDER_EXTERNAL_URL: str = ""
    
    model_config = {"env_file": ".env"}

settings = Settings()