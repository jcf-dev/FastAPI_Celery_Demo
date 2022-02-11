from fastapi import APIRouter

from app.views.rest import generate_email, users

router = APIRouter()

router.include_router(generate_email.router, prefix='/generate_email_address')
router.include_router(users.router, prefix='/users')
