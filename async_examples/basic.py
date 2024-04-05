import asyncio


async def async_add(a, b):
    print("Starting async_add")
    await asyncio.sleep(5)  # Simulate an async operation
    print("Result From async_add", a + b)
    return a + b


async def async_sub(a, b):
    print("Starting async_sub")
    print("Result From async_sub", a - b)
    return a - b


async def main():
    # Schedule both async_add and async_sub to run concurrently.
    res_add, res_b = await asyncio.gather(
        async_add(1, 2),  # Pass the first function call
        async_sub(1, 2),  # Pass the second function call
    )


if __name__ == "__main__":
    asyncio.run(main())
