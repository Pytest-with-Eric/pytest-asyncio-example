from pathlib import Path
import pytest
from async_application.core import upload_file, main

home = str(Path.home())

@pytest.mark.asyncio
async def test_upload_file():
    result_upload = await upload_file(file_name=f"{home}/sample.jpeg")
    assert result_upload["status"] is True


# @pytest.mark.asyncio
# async def test_upload_file():

