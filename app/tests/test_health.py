import pytest
from fastapi import FastAPI, status
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health(client: AsyncClient, app: FastAPI) -> None:
    """
    Checks the health endpoint.

    :param client: client for the app.
    :param app: current FastAPI application.
    """
    url = app.url_path_for("health")
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK
