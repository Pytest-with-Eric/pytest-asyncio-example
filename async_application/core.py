# Spec 1. Upload a large file via HTTP Request 2. Write to DB   3.???

import logging
import requests
from pathlib import Path

home = str(Path.home())

# Set Logging
logging.basicConfig(level=logging.INFO)


def upload_file(file_name: str = None) -> str:
    """
    Function to call the API via the Requests Library
    :param file_name: Filename, Str
    :return: Response. Type - JSON Formatted String
    """
    try:
        files = {
            "file": open(file_name, 'rb'),
        }
        endpoint = "https://api.anonfiles.com/upload"
        response = requests.post(endpoint, files=files)
        response_json = response.json()
        logging.info(f"Response from API: {response_json}")
        if response.status_code in (200, 201) \
                and response_json["status"] is True:
            return response_json
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        logging.error(errh)
    except requests.exceptions.ConnectionError as errc:
        logging.error(errc)
    except requests.exceptions.Timeout as errt:
        logging.error(errt)
    except requests.exceptions.RequestException as err:
        logging.error(err)


upload_file(file_name=f"{home}/sample.jpeg")