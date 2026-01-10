from pydantic_settings import BaseSettings
from typing import Optional
from dotenv import load_dotenv
import os

# Explicitly load the .env file
load_dotenv()

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # JWT settings
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # API settings
    API_PREFIX: str = os.getenv("API_PREFIX", "/api/v1")

    # Logging settings
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
