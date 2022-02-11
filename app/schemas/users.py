from typing import Optional

from pydantic import BaseModel, EmailStr


# Base Schema for User
class _UserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_active: Optional[bool] = False
    is_superuser: Optional[bool] = False


class UserLogin(BaseModel):
    username: str
    password: str


class UserCreate(_UserBase):
    username: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = False
    is_superuser: Optional[bool] = False


class UserUpdate(_UserBase):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_active: Optional[bool] = False
    is_superuser: Optional[bool] = False


# Base DB Schema for UserID
class _UserInDBBase(_UserBase):
    id: Optional[int]

    class Config:
        orm_mode = True


class User(_UserInDBBase):
    pass


class UserInDB(_UserInDBBase):
    password: str
