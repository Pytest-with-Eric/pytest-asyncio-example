import asyncio
import aiohttp


async def async_add(a, b):
    await asyncio.sleep(1)  # Simulate an async operation
    return a + b
