from collections.abc import AsyncGenerator  # noqa
import uuid  # noqa

from sqlalchemy import Column, String, Text, DateTime, ForeignKey  # noqa

from sqlalchemy.dialects.postgresql import UUID  # noqa

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker  # noqa

from sqlalchemy.orm import DeclarativeBase, relationship  # noqa

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

