import pytest
import asyncio
import pytest_asyncio
from async_examples.basic import async_add


# Basic Async test function
@pytest.mark.asyncio
async def test_async_add():
    result = await async_add(1, 2)
    assert result == 3


# Async fixtures
@pytest_asyncio.fixture
async def loaded_data():
    await asyncio.sleep(1)  # Simulate loading data asynchronously
    return {"key": "value"}


# Async test functions with fixtures
@pytest.mark.asyncio
async def test_fetch_data(loaded_data):
    assert loaded_data["key"] == "value"
