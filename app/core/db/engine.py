import logging

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.conf import settings

engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True  # https://docs.sqlalchemy.org/en/14/core/pooling.html#dealing-with-disconnects
)

async_session = sessionmaker(
    engine,
    expire_on_commit=True,
    class_=AsyncSession
)


async def get_db() -> AsyncSession:
    session = async_session()
    try:
        yield session
    except SQLAlchemyError as e:
        await session.rollback()
        logging.error(e)
    finally:
        await session.close()
