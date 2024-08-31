#importing module
from src.musicgenre.entity import DataIngestionConfig, DataIngestionArtifact
from src.musicgenre.exception import music_genre_exception
from src.musicgenre.constants import *
from src.musicgenre.logger import logging
from src.musicgenre.utils import *
import numpy as np
import gdown
import pandas as pd

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20} Data Ingestion log started. {'<<'*20}")
            self.data_ingestion_config=data_ingestion_config
            os.makedirs(self.data_ingestion_config.raw_data_dir,exist_ok=True)
            self.output_path=os.path.join(self.data_ingestion_config.raw_data_dir,"data.csv")
        except Exception as e:
            raise music_genre_exception(e,sys) from e
        
    def __get_data_from_gdrive(self):
        try:
            gdown.download(DRIVE_LINK, self.output_path, quiet=False)
            logging.info(f"Data downloaded from Google Drive: {self.output_path}")
        except Exception as e:
            raise music_genre_exception(e,sys) from e


    def initiate_data_ingestion(self):
        try:
            self.__get_data_from_gdrive()
            return DataIngestionArtifact(raw_data_file_path=self.output_path,message="Data Ingestion completed successfully")
        except Exception as e:
            raise music_genre_exception(e,sys) from e
    def __del__(self):
        logging.info(f"{'>>'*20} Data Ingestion log completed. {'<<'*20}")






