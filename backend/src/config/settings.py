from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database settings
    DATABASE_URL: str = "postgresql://neondb_owner:npg_4I5PiDrQsaYn@ep-soft-bar-ahmccume-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

    # JWT settings
    SECRET_KEY: str = "qP7YxJcP0V9W9G8n4Hf6rA0wK2mN5LxE8ZsQyJ1U"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Environment
    ENVIRONMENT: str = "development"

    # API settings
    API_PREFIX: str = "/api/v1"

    # Logging settings
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()