import pytest
from httpx import AsyncClient
from web_app.api.main import app

@pytest.mark.asyncio
async def test_body_size_limit_exceeds_1mb():
    # Generate a payload slightly larger than 1MB (1,048,577 bytes)
    payload = b"a" * (1024 * 1024 + 1)
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/health", content=payload)
    assert response.status_code == 413

@pytest.mark.asyncio
async def test_body_size_limit_within_1mb():
    # Generate a payload within 1MB
    payload = b"a" * 100
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/health", content=payload)
    # The response code should not be 413. Since it is /health and doesn't support POST,
    # it might return 405 Method Not Allowed or similar, but NOT 413.
    assert response.status_code != 413

@pytest.mark.asyncio
async def test_body_size_limit_chunked_exceeds_1mb():
    # Stream payload chunked, total exceeding 1MB
    async def chunk_generator():
        yield b"a" * (512 * 1024)
        yield b"a" * (512 * 1024 + 1)
    
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/health", content=chunk_generator())
    assert response.status_code == 413
