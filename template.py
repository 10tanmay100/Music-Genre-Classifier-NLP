# importing libraries
import os
from pathlib import Path

#defining the package name
PackageName="musicgenre"

#lists of files and directories that we want to create
list_of_files=[
    ".github/workflows/.gitkeep", # for our github actions
    f"src/{PackageName}/logger.py", # Script for logging
    f"src/{PackageName}/exception.py", # script for custom exception
    f"src/{PackageName}/__init__.py", # initialization file for the package
    f"src/{PackageName}/components/__init__.py", # initialization file for components
    f"src/{PackageName}/utils/__init__.py", # initialization file for utility functions
    f"src/{PackageName}/utils/helper.py",
    f"src/{PackageName}/config/__init__.py", # scripts for configuration
    f"src/{PackageName}/pipeline/__init__.py", # scripts for running pipeline
    f"src/{PackageName}/entity/__init__.py", # scripts for our stage entities
    f"src/{PackageName}/constants/__init__.py", # scripts for constants things in our code,
    "tests/_init__.py", # for test cases,
    "tests/unit/__init__.py", # for unit tests
    "configs/config.yaml", # yamlfile for configuration
    "dvc.yaml", # a yamlfile for data version control
    "params.yaml", # a yamlfile for parameters
    "init_setup.sh", # a bashfile for initialization
    "requirements.txt", # a txtfile for dependencies
    "setup.py", # a pyfile for building our package
    "research/experiment.ipynb", # ipynb file for experiments
    "main.py", #for testing our stages
]

for filepath in list_of_files:
    #convert the filepath to a Path object for easier manipulation
    filepath=Path(filepath)

    #Extract the directory and filename fromt the file path
    filedir, filename=os.path.split(filepath)

    # create the directory if it doesn't exist
    if filedir:
        os.makedirs(filedir,exist_ok=True)
    
    # create an empty file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w') as f:
            pass

    else:
        print(f"{filename} already exists..")







