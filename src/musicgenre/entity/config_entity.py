# importing libraries
from collections import namedtuple


DataIngestionConfig= namedtuple('DataIngestionConfig',["raw_data_dir"])
TrainingPipelineConfig= namedtuple('TrainingPipelineConfig',["artifact_dir"])
DataValidationConfig= namedtuple('DataValidationConfig',["raw_data_path","schema_path"])








