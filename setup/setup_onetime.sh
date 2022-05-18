cd ..
sudo apt install python3 python3-tk
python3 -m pip install virtualenv
python3 -m venv venv

source ./venv/bin/activate
python3 -m pip install -r setup/requirements.txt

mkdir DataCollected
