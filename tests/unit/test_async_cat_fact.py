import pytest
import asyncio
from asyncmock import AsyncMock


@pytest.mark.asyncio
async def test_get_cat_fact_fixture(async_app_client) -> None:
    """
    Test for get_cat_fact method using Async Fixture
    :param async_app_client:
    :return: None
    """
    task1 = asyncio.create_task(async_app_client.get_cat_fact())

    value_task1 = await task1
    print(value_task1)


@pytest.fixture
def mock_thing() -> AsyncMock:
    """
    Async Mock Fixture
    :return:
    """
    mock_thing = AsyncMock()
    mock_thing.CatFact.get_cat_fact = AsyncMock(
        return_value="Mother cats " "teach their kittens " "to use the litter box."
    )
    return mock_thing


@pytest.mark.asyncio
async def test_get_cat_fact_mock(mock_thing) -> None:
    """
    Test for get_cat_fact method using Async Mocking
    :param mock_thing: Mock fixture
    :return: None
    """
    result = await mock_thing.CatFact.get_cat_fact()
    assert result == "Mother cats teach their kittens to use the litter box."
