from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from core.settings.settings import settings

async_engine: AsyncEngine = create_async_engine(settings.postgres.async_url, echo=True)
async_postgres_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    autoflush=False,
    future=True,
)


async def get_async_postgres_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_postgres_session() as session:
        yield session
