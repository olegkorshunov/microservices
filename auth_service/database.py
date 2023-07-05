from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from auth_service.config import settings


class Base(DeclarativeBase):
    pass


async_engine = create_async_engine(settings.DATABASE_URL)
async_session_maker = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
