# importing our required modules
from src.musicgenre.entity import DataIngestionConfig, TrainingPipelineConfig
from src.musicgenre.logger import logging
from src.musicgenre.exception import music_genre_exception
from src.musicgenre.constants import *
from src.musicgenre.utils import *
import os, sys

class Configuration:
    def __init__(self, config_file_path: str=CONFIG_FILE_PATH,current_time_stamp:str=CURRENT_TIME_STAMP):
        try:
            self.config_info=read_yaml(config_file_path)
            self.training_pipeline_config=self.get_training_pipeline_config()
            self.timestamp=current_time_stamp
        except Exception as e:
            raise music_genre_exception(e,sys) from e

    def get_data_ingestion_config(self):
        try:
            data_ingestion_info=self.config_info[DATA_INGESTION_CONFIG_KEY]
            artifact_dir=self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir=os.path.join(artifact_dir,DATA_INGESTION_ARTIFACT_DIR,self.timestamp)
            raw_data_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])

            data_ingestion_config=DataIngestionConfig(raw_data_dir=raw_data_dir)
            logging.info(f"Data ingestion config: {data_ingestion_config}")
            return data_ingestion_config

            
        except Exception as e:
            raise music_genre_exception(e,sys) from e

    def get_training_pipeline_config(self):
        try:
            training_pipeline_config=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir=os.path.join(ROOT_DIR,training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            training_pipeline_config=TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipeline config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise music_genre_exception(e,sys) from e









