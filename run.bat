@echo off
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install tensorflow numpy opencv-python scikit-learn
python database.py
python voting_system.py
pause
