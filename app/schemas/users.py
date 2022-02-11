from typing import Optional

from pydantic import BaseModel, EmailStr


# Base Schema for User
class _UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = False
    is_superuser: Optional[bool] = False
    username: Optional[str] = None


class UserCreate(_UserBase):
    username: str
    email: EmailStr
    password: str
    is_active: bool
    is_superuser: bool


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
    hashed_password: str
