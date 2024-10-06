import yaml
from src.musicgenre.exception import music_genre_exception
import os, sys
from src.musicgenre.logger import logging
import re
import requests


def read_yaml(filepath:str):
    try:
        with open(filepath, 'rb') as ymlfile:
            return yaml.safe_load(ymlfile)
    except Exception as e:
        raise music_genre_exception(e,sys) from e


def extract_file_id(google_drive_link):
    try:
        file_id_match=re.search(r'/d/([a-zA-Z0-9_-]+)',google_drive_link)
        if file_id_match:
            logging.info(f"File ID extracted from the link: {file_id_match.group(1)}")
            return file_id_match.group(1)
    except Exception as e:
        raise music_genre_exception(e,sys) from e

def download_csv_from_gdrive(google_drive_link,destination):
    try:
        file_id=extract_file_id(google_drive_link)

        url=f"https://drive.google.com/uc?id={file_id}"

        response=requests.get(url,stream=True)

        if response.status_code==200:
            with open(destination, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print("File download complete")

        
    except Exception as e:
        raise music_genre_exception(e,sys) from e



