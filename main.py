# importing libraries
from src.musicgenre.pipeline import Pipeline
from src.musicgenre.config.configuration import Configuration



def main():
    pipeline=Pipeline(Configuration)
    print(pipeline.run_pipeline())



if __name__=="__main__":
    main()