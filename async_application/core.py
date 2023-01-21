# Spec 1. Upload a large file via HTTP Request 2. Write to Disk
import json
import logging
import uuid
from datetime import datetime
import requests
import asyncio

# Set Logging
logging.basicConfig(level=logging.INFO)


async def upload_file(file_name: str = None) -> dict:
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
        logging.info(f"Uploading File `{file_name}` to Server...")
        response = requests.post(endpoint, files=files)
        await asyncio.sleep(3)  # TODO REMOVE
        response_json = response.json()
        logging.debug(f"Response from API: {response_json}")
        if response.status_code in (200, 201) \
                and response_json["status"] is True:
            logging.info(f"File `{file_name}` successfully uploaded to Server!!!")
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


async def save_to_disk() -> bool:
    """
    Function to save a dict to disk as a JSON file
    :return: Bool
    """
    sample = {
        "Value": str(uuid.uuid4()),
        "Time": str(datetime.utcnow())
    }
    with open(f"./tests/unit/tmp_data/{str(uuid.uuid4())}.json", 'w', encoding='utf-8') as f:
        json.dump(sample, f, ensure_ascii=False, indent=4)
        logging.info("Data Saved to Disk!!!")
        status = True
    return status
