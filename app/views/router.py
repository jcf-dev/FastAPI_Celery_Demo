from fastapi import APIRouter

from app.views.rest import generators, users

router = APIRouter()

router.include_router(generators.router, prefix='/generate')
router.include_router(users.router, prefix='/users')
