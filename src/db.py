from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from .db_config import settings

sync_engine = create_engine(
    settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10,
)
async_engine = create_async_engine(
    settings.DATABASE_URL_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10,
)

sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

Session = sessionmaker(sync_engine)


class Base(DeclarativeBase):
    pass
