#importing module
from src.musicgenre.config.configuration import Configuration
from src.musicgenre.entity import DataIngestionConfig, TrainingPipelineConfig, DataIngestionArtifact
from src.musicgenre.logger import logging
from src.musicgenre.components import DataIngestion
from src.musicgenre.exception import music_genre_exception
from src.musicgenre.constants import *
from src.musicgenre.utils import *
import os,sys


class Pipeline:
    def __init__(self, config: Configuration):
        self.config = config()
    def start_data_ingestion(self):
        try:
            data_ingestion=DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise music_genre_exception(e,sys) from e
        

    def run_pipeline(self):
        try:
            data_ingestion_process=self.start_data_ingestion()
            return "completed"
        except Exception as e:
            raise music_genre_exception(e,sys) from e




