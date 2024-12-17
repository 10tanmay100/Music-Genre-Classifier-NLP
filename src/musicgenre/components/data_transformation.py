from src.musicgenre.entity import DataIngestionConfig, DataIngestionArtifact, DataValidationConfig,DataValidationArtifact,DataTransformationConfig,DataTransformationArtifact
from src.musicgenre.exception import music_genre_exception
from src.musicgenre.constants import *
from src.musicgenre.logger import logging
from src.musicgenre.utils import *
import numpy as np
import pandas as pd
import pickle
import shutil
# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
import warnings
warnings.filterwarnings(action="ignore")
nltk.download('stopwords')
from nltk.corpus import stopwords
from wordcloud import WordCloud
from nltk.stem.porter import PorterStemmer
import re
from sklearn.preprocessing import LabelEncoder
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import CountVectorizer





class DataTransformation:

    def __init__(self,data_transformation_config:DataTransformationConfig,
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_artifact: DataValidationArtifact):
        try:
            logging.info(f"{'>>'*20} Data Transformation log started. {'<<'*20}")
            self.data_transformation_config=data_transformation_config
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_artifact=data_validation_artifact
        except Exception as e:
            raise music_genre_exception(e,sys) from e
        
    def get_transformer_object_and_test_train_dir(self):
        try:
            os.makedirs(self.data_transformation_config.transformed_train_dir,exist_ok=True)
            logging.info(f"Train Directory Created-->{self.data_transformation_config.transformed_train_dir}")

            os.makedirs(self.data_transformation_config.transformed_test_dir,exist_ok=True)
            logging.info(f"Test Directory Created-->{self.data_transformation_config.transformed_test_dir}")


            os.makedirs(self.data_transformation_config.preprocessed_object_folder_path,exist_ok=True)
            logging.info(f"Preprocessing folder path Created-->{self.data_transformation_config.preprocessed_object_folder_path}")

            if self.data_validation_artifact.is_validated:
                df=pd.read_csv(self.data_validation_artifact.validated_csv_path)
                df=df.drop(["id"],axis=1)

                                # cleaning the dataset
                corpus=[]

                #initialize the stemmer class
                stemmer = PorterStemmer()

                for row in tqdm(range(df.shape[0])):
                    # removing non alphabetic characters
                    data=re.sub(pattern='[^a-zA-Z]',repl=" ",string=df.iloc[row,0])
                    # converting all the words to lower case
                    lower_case_data=data.lower()
                    # tokenizing words
                    token_word=lower_case_data.split()
                    # removing stop words
                    removed_stop_words=[word for word in token_word if word not in stopwords.words("english")]
                    # stemming tokens
                    stemmed_words=[stemmer.stem(word) for word in removed_stop_words]
                    # joining the stemmed words back to string
                    final_script = " ".join(stemmed_words)
                    # appending the final corpus
                    corpus.append(final_script)

                ## converting our corpus into numbers
                cv=CountVectorizer(max_features=50000)
                input=cv.fit_transform(corpus).toarray()
                # applying label encoder on target 
                lblen=LabelEncoder()
                output=lblen.fit_transform(df["genre"])
                # building a model
                Xtrain,Xtest,Ytrain,Ytest= train_test_split(input,output,test_size=0.1,random_state=12)
                print(f"Xtrain size {Xtrain.shape} and Xtest size {Xtest.shape}")
                logging.info(f"XTrain size {Xtrain.shape} and XTest size {Xtest.shape}")

                print(96)
                train_df=pd.DataFrame(Xtrain)
                train_df["label"]=Ytrain
                print(99)
                test_df=pd.DataFrame(Xtest)
                test_df["label"]=Ytest
                print(102)
                #store the data inside data
                data_path=os.path.join("data","features")
                os.makedirs(data_path,exist_ok=True)
                train_df.to_csv(os.path.join(self.data_transformation_config.transformed_train_dir,"train.csv"),index=False)
                test_df.to_csv(os.path.join(self.data_transformation_config.transformed_test_dir,"test.csv"),index=False)
            path_pkl= self.data_transformation_config.preprocessed_object_file_path

            with open(path_pkl, 'wb') as file:
                pickle.dump(cv,file)
                print(112)
            return DataTransformationArtifact(
                is_transformed=True,message="Data Transformed",transformed_train_file_path=os.path.join(self.data_transformation_config.transformed_train_dir,"train.csv"),transformed_test_file_path=os.path.join(self.data_transformation_config.transformed_test_dir,"test.csv"),
                preprocessed_object_file_path=self.data_transformation_config.preprocessed_object_file_path
            )
        except Exception as e:
            raise music_genre_exception(e,sys) from e
        
    def initiate_data_transformation(self):
        try:
            data_transformation_artifact=self.get_transformer_object_and_test_train_dir()
            logging.info(f"data transformation artifact: {data_transformation_artifact}")
            return data_transformation_artifact
        except Exception as e:
            raise music_genre_exception(e,sys) from e
        
    def __del__(self):
        logging.info(f"{'>>'*20} Data Transformation log completed. {'<<'*20}")


