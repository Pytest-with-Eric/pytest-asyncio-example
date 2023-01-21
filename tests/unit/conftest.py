import pytest
import pytest_asyncio
from async_application.core_class import AsyncApp


@pytest_asyncio.fixture()
async def async_app_client():
    async_app = AsyncApp()
    yield async_app
