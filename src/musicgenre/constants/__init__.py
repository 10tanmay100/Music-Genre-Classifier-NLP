# importing libraries
import os
from datetime import datetime


def get_current_time():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

#overall constant requirements
ROOT_DIR=os.getcwd()
CURRENT_TIME_STAMP=get_current_time()
CONFIG_FILE_PATH="C:/Learning Content/DS/NLP/Yt Projects/Movie Genre Classifier/configs/config.yaml"


#pipeline constant requirements
TRAINING_PIPELINE_CONFIG_KEY="training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY="artifact_dir"
TRAINING_PIPELINE_NAME_KEY="pipeline_name"

# Data Ingestion constant requirements
DATA_INGESTION_CONFIG_KEY="data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR="data_ingestion"
DATA_INGESTION_RAW_DATA_DIR_KEY="raw_data_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY="ingested_dir"


DRIVE_LINK="https://drive.google.com/file/d/1FME9CmFwcWFJPUK_syJigJYLiRXpKiAg/view?usp=sharing"



