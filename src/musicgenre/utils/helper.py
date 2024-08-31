import yaml
from src.musicgenre.exception import music_genre_exception
import os, sys


def read_yaml(filepath:str):
    try:
        with open(filepath, 'rb') as ymlfile:
            return yaml.safe_load(ymlfile)
    except Exception as e:
        raise music_genre_exception(e,sys) from e








