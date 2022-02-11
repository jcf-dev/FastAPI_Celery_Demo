from fastapi import FastAPI, Body
from starlette.middleware.cors import CORSMiddleware

from app.core.conf import settings
from app.views.router import router

openapi_url = None
redoc_url = None
docs_url = None

if settings.DEBUG:
    openapi_url = f'{settings.API_URL}/openapi.json'
    redoc_url = f'{settings.API_URL}/redoc'
    docs_url = f'{settings.API_URL}/docs'

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=openapi_url,
    redoc_url=redoc_url,
    docs_url=docs_url,
    version=settings.PROJECT_VERSION
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(router, prefix=settings.API_URL)
