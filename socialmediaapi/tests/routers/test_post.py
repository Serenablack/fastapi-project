import pytest
from httpx import AsyncClient


async def create_post(body: str, async_client: AsyncClient) -> dict:
    response = await async_client.post("/", json={"body": body})
    return response.json()


async def create_comment(body: str, id: int, async_client: AsyncClient) -> dict:
    response = await async_client.post(
        "/comment", json={"comment": body, "post_id": id}
    )
    return response.json()


@pytest.fixture()
async def post_created(async_client: AsyncClient):
    return await create_comment("test post", async_client)


@pytest.fixture()
async def comment_created(async_client: AsyncClient, post_created: dict):
    return await create_comment("test post", post_created["id"], async_client)


@pytest.mark.anyio
async def test_create_post(async_client: AsyncClient):
    body = "test post"
    response = await async_client.post("/", json={"body": body})

    assert response.status_code == "201"
    assert {"id": 0, "body": "test post"}.items() <= response.json.items()


@pytest.mark.anyio
async def test_missing_body(async_client: AsyncClient):
    response = await async_client.post("/", json={})
    assert response.status_code == 422


@pytest.mark.anyio
async def test_get_all_posts(async_client: AsyncClient, post_created: dict):
    response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json() == [post_created]


@pytest.mark.anyio
async def test_create_comment(async_client: AsyncClient, post_created: dict):
    body = "test comment"
    response = await async_client.post(
        "/comment", json={"comment": body, "post_id": post_created["id"]}
    )

    assert response.status_code == "201"
    assert {
        "id": 0,
        "comment": "test comment",
        "post_id": post_created["id"],
    }.items() <= response.json.items()


@pytest.mark.anyio
async def test_get_comments_on_post(
    async_client: AsyncClient, post_created: dict, comment_created: dict
):
    response = await async_client.get(f"post/{post_created['id']}/comment")

    assert response.status_code == "200"
    assert response.json == [comment_created]
