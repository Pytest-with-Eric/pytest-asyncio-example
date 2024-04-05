import pytest
import pytest_asyncio
from asyncmock import AsyncMock
from async_examples.cat_fact import CatFact


@pytest_asyncio.fixture
async def cat_fact():
    return CatFact()


# Test with Real API call (Not Recommended)
@pytest.mark.asyncio
async def test_get_cat_fact(cat_fact):
    result = await cat_fact.get_cat_fact()
    print(result)
    assert result["status"] == 200
    assert "data" in result["result"]


# Test with Mocked API call (Recommended when interacting with external services)
@pytest.mark.asyncio
async def test_get_cat_fact_mocked(mocker):
    # Mock the get_cat_fact method of CatFact
    mock_response = {"status": 200, "result": {"data": "Cats are awesome!"}}
    mocker.patch.object(CatFact, "get_cat_fact", AsyncMock(return_value=mock_response))

    cat_fact_instance = CatFact()
    result = await cat_fact_instance.get_cat_fact()

    assert result["status"] == 200
    assert "data" in result["result"]
    assert result["result"]["data"] == "Cats are awesome!"
