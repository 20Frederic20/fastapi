from pydantic import PostgresDsn, RedisDsn, model_validator
from pydantic_settings import BaseSettings
from .constants import Environment
from typing import Optional


class Config(BaseSettings):
    SITE_DOMAIN: str = "myapp.com"

    # ENVIRONMENT: Environment = Environment.PRODUCTION

    SENTRY_DSN: str | None = None

    CORS_ORIGINS: list[str] = ["*"]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str] = ["*"]

    APP_VERSION: str = "1.0"

    PROJECT_NAME: str = "MyFastAPIProject"
    DATABASE_URL: str = "postgresql://postgres:+012345678!@localhost:5433/fastapi"
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"


settings = Config()
