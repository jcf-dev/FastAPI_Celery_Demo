import secrets
import os
import time

from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class AsyncPostgresDsn(PostgresDsn):
    allowed_schemes = {'postgresql+asyncpg'}


class Settings(BaseSettings):

    # Core Settings
    PROJECT_NAME: str = 'FastAPI Celery Demo'
    PROJECT_VERSION: str = '0.1.0'
    SERVER_NAME: str = 'fastapi-celery-demo'
    DEBUG: bool = True

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    ROOT_DIR: Path = Path(BASE_DIR).parent

    # Endpoint Settings
    SERVER_HOST: AnyHttpUrl = 'http://localhost:8000'
    API_URL: str = '/api/' + os.getenv('API_VERSION')
    GRAPHQL_API: bool = False  # GraphQL API Switch
    GRAPHQL_APP: bool = False  # GraphQL APP Switch

    # Security Settings
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:8000"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost:8000']

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(
            cls,
            v: Union[str, List[str]]
    ) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER')
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT')

    SQLALCHEMY_DATABASE_URI: Optional[AsyncPostgresDsn] = None

    @validator('SQLALCHEMY_DATABASE_URI', pre=True)
    def assemble_db_connection(
            cls,
            v: Optional[str],
            values: Dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        return AsyncPostgresDsn.build(
            scheme='postgresql+asyncpg',
            user=values.get('POSTGRES_USER'),
            password=values.get('POSTGRES_PASSWORD'),
            host=values.get('POSTGRES_SERVER'),
            port=values.get('POSTGRES_PORT'),
            path=f"/{values.get('POSTGRES_DB') or ''}"
        )

    class Config:
        case_sensitive = True


settings = Settings()
