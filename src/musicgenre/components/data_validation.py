#importing module
from src.musicgenre.entity import DataIngestionConfig, DataIngestionArtifact, DataValidationConfig,DataValidationArtifact
from src.musicgenre.exception import music_genre_exception
from src.musicgenre.constants import *
from src.musicgenre.logger import logging
from src.musicgenre.utils import *
import numpy as np
import pandas as pd


class DataValidation:

    def __init__(self,data_validation_config:DataValidationConfig,data_ingestion_artifact:DataIngestionArtifact):

        try:
            logging.info(f"{'>>'*20} Data Validation log started. {'<<'*20}")
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
            self.timestamp=f"{datetime.now().strftime('%Y-%m-%d_%H%M%S')}"
        except Exception as e:
            raise music_genre_exception(e,sys) from e
        
    def __validate_dataset_schema(self):
        try:
            validation_status=False
            logging.info(f"Validating dataset schema against configuration.")
            df=pd.read_csv(self.data_ingestion_artifact.raw_data_file_path)

            l=[]
            for cols in df.columns:
                yaml=read_yaml(self.data_validation_config.schema_path)
                if cols in yaml.keys():
                    if str(df[cols].dtype)==yaml[cols]:
                        l.append(True)
            if len(l)==len(yaml.keys()):
                validation_status=True
                logging.info(f"Dataset schema validation passed.")
            if validation_status==True:
                os.makedirs(self.data_validation_config.raw_data_path,exist_ok=True)
                df.to_csv(os.path.join(self.data_validation_config.raw_data_path,"validated_data.csv"),index=False)
            return validation_status
        except Exception as e:
            raise music_genre_exception(e,sys) from e
        
    def initiate_data_validation(self):
        try:
            status=self.__validate_dataset_schema()
            data_validation_artifact=DataValidationArtifact(
                validated_csv_path=os.path.join(self.data_validation_config.raw_data_path,"validated_data.csv"),
                is_validated=status,
                message="Data Validation Performed"
            )
            logging.info("Data Validation artifact: %s",data_validation_artifact)
        except Exception as e:
            raise music_genre_exception(e,sys) from e
    def __del__(self):
        logging.info(f"{'>>'*20} Data Validation log completed. {'<<'*20}")


