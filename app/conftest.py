import asyncio
from typing import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from core.app import get_app
from db.db import async_engine
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession


@pytest.fixture(scope="session")
def event_loop(request) -> Generator:  # : indirect usage
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def client(app: FastAPI) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest_asyncio.fixture
def app() -> FastAPI:
    return get_app()


@pytest_asyncio.fixture(scope="function")
async def db_session() -> AsyncGenerator:
    session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
    async with session() as s:
        async with async_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

        yield s

    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

    await async_engine.dispose()
