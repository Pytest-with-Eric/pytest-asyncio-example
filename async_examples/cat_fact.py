import logging
import aiohttp
import asyncio


class CatFact:
    def __init__(self):
        self.base_url = "https://meowfacts.herokuapp.com/"

    async def get_cat_fact(self):
        """
        Asynchronously get a Cat Fact from Rest API and return a dict with status and fact.
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.base_url) as response:
                    if response.status in (200, 201):
                        json_response = await response.json()
                        return {"status": response.status, "result": json_response}
                    else:
                        return {
                            "status": response.status,
                            "error": "Cat Fact Not Available",
                        }
        except aiohttp.ClientError as err:
            logging.error(f"Client error: {err}")
            return {"status": 500, "error": "Failed to fetch Cat Fact"}
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return {"status": 500, "error": "Failed to fetch Cat Fact"}


async def main():
    cat_fact = CatFact()
    result = await cat_fact.get_cat_fact()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
