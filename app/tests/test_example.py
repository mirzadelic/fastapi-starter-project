import pytest
from db.models.example import Example
from fastapi import FastAPI, status
from httpx import AsyncClient
from sqlalchemy import func, select
from sqlmodel.ext.asyncio.session import AsyncSession


@pytest.mark.asyncio
async def test_list_example_empty(
    client: AsyncClient,
    app: FastAPI,
    db_session: AsyncSession,
) -> None:
    """
    Checks empty list of example
    """
    url = app.url_path_for("get_examples")
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


@pytest.mark.asyncio
async def test_list_example(
    client: AsyncClient,
    app: FastAPI,
    db_session: AsyncSession,
) -> None:
    """
    Checks list of example
    """
    example_data = {"name": "Example 1", "active": True}
    example = Example(**example_data)
    db_session.add(example)
    await db_session.commit()

    url = app.url_path_for("get_examples")
    response = await client.get(url)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == example_data["name"]
    assert data[0]["active"] == example_data["active"]


@pytest.mark.asyncio
async def test_create_example(
    client: AsyncClient,
    app: FastAPI,
    db_session: AsyncSession,
) -> None:
    """
    Checks create of example
    """
    example_data = {"name": "Example 1", "active": True}

    url = app.url_path_for("get_examples")
    response = await client.post(url, json=example_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["name"] == example_data["name"]
    assert data["active"] == example_data["active"]
    count = await db_session.execute(select([func.count()]).select_from(Example))
    assert count.scalar() == 1
