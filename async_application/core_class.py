import json
import logging
import requests


class AsyncApp:
    def __init__(self):
        self.base_url = "https://meowfacts.herokuapp.com/"

    async def get_cat_fact(self) -> tuple[int, dict] | str:
        """
        Function to get a Cat Fact from Rest API
        :return: JSON Encoded Response String
        """
        try:
            response = requests.get(self.base_url)
            if response.status_code in (200, 201):
                return response.status_code, response.json()
            else:
                return json.dumps({"ERROR": "Cat Fact Not Available"})
        except requests.exceptions.HTTPError as errh:
            logging.error(errh)
        except requests.exceptions.ConnectionError as errc:
            logging.error(errc)
        except requests.exceptions.Timeout as errt:
            logging.error(errt)
        except requests.exceptions.RequestException as err:
            logging.error(err)