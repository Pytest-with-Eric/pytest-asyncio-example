import pytest
import pytest_asyncio
from async_application.cat_fact import CatFact


@pytest_asyncio.fixture()
async def async_app_client():
    async_cat_fact = CatFact()
    yield async_cat_fact
