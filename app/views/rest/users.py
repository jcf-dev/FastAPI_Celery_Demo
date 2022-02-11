from fastapi import APIRouter, Depends, HTTPException

from app.core.security.auth import AuthHandler
from app.schemas import UserLogin, UserCreate, UserUpdate, User
from app.models import User

router = APIRouter()

auth_handler = AuthHandler()
users = []


@router.post('/register', tags=['user'], status_code=201)
async def register(user_create: UserCreate):
    if any(x['username'] == user_create.username for x in users):
        raise HTTPException(status_code=400, detail='Username is Taken')
    hashed_password = auth_handler.get_password_hash(user_create.password)
    users.append({
        'username': user_create.username,
        'password': hashed_password
    })
    return


@router.post('/login', tags=['user'])
async def login(user_login: UserLogin):
    user = None
    for x in users:
        if x['username'] == user_login.username:
            user = x
            break
    if (user is None) or (not auth_handler.verify_password(user_login.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user['username'])
    return {'token': token}


@router.get('/me', tags=['user'])
async def me(username=Depends(auth_handler.auth_wrapper)):
    return {'username': username}
