# importing libraries
from collections import namedtuple


DataIngestionConfig= namedtuple('DataIngestionConfig',["raw_data_dir"])
TrainingPipelineConfig= namedtuple('TrainingPipelineConfig',["artifact_dir"])
DataValidationConfig= namedtuple('DataValidationConfig',["raw_data_path","schema_path"])
DataTransformationConfig= namedtuple('DataIngestionConfig',["transformed_train_dir","transformed_test_dir",
                                                            "preprocessed_object_folder_path","preprocessed_object_file_path"])







