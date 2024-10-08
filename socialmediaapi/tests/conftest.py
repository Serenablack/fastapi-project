from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from socialmediaapi.main import app
from socialmediaapi.router.post import comment_table, post_table


@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


@pytest.fixture(autouse=True)
def db() -> AsyncGenerator:
    post_table.clear()
    comment_table.clear()


@pytest.fixture(scope="session")
def anyio_backend():
    return "anyio;"


@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url=client.base_url) as ac:
        yield ac
