from fastapi import APIRouter

from app.views.rest import generate_email

router = APIRouter()

router.include_router(generate_email.router, prefix='/generate_email_address')
