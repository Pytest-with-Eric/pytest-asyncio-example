from pathlib import Path
import pytest
import asyncio
from async_application.core import upload_file, save_to_disk

home = str(Path.home())


@pytest.mark.asyncio
async def test_upload_file():
    result_upload = await upload_file(file_name=f"{home}/sample.jpeg")
    assert result_upload["status"] is True


@pytest.mark.asyncio
async def test_save_to_disk():
    result_save = await save_to_disk()
    assert result_save is True


@pytest.mark.asyncio
async def test_main():
    task1 = asyncio.create_task(upload_file(file_name=f"{home}/sample.jpeg"))
    task2 = asyncio.create_task(save_to_disk())

    value_task1 = await task1
    value_task2 = await task2

    assert value_task1["status"] is True
    assert value_task2 is True
