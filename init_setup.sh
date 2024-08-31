echo [$(date)]: "STARTING THE PROCESS"
echo [$(date)]: "Creating Python Environment 3.9"
conda create --prefix ./venv python=3.9 -y
echo [$(date)]: "Activating Python Environment 3.9"
source Activate ./venv
echo [$(date)]: "Installing Development Requirements"
pip install -r requirements.txt
echo [$(date)]: "ENDING THE PROCESS"