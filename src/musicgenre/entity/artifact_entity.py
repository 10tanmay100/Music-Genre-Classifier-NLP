#importing libraries
from collections import namedtuple



DataIngestionArtifact = namedtuple("DataIngestionArtifact",["raw_data_file_path","message"])
DataValidationArtifact = namedtuple("DataValidationArtifact",["validated_csv_path","is_validated","message"])