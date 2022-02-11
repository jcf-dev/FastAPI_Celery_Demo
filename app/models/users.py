from sqlalchemy import Column, Boolean, String

from app.core.db.base_class import Base


class User(Base):
    username = Column(String(256), index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
