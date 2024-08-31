# importing libraries
import logging
from datetime import datetime
import os
import pandas as pd

#defining the logging folder name
LOG_DIR="music-genre-logs"

# getting the current timestamp
CURRENT_TIMESTAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
# getting the logfile name
LOG_FILE_NAME = f"log_{CURRENT_TIMESTAMP}.log"
# creating the directory for log files
os.makedirs(LOG_DIR,exist_ok=True)
#defining the complete logfiles path
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

#setting loggging
logging.basicConfig(filename=LOG_FILE_PATH,filemode="w",format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.INFO)









