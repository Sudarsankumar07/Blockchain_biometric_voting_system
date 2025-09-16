@echo off
REM -----------------------------------------------------------------------------
REM Blockchain Biometric Voting System - Setup and Run Script (Windows)
REM -----------------------------------------------------------------------------
REM This script will:
REM   1. Create a Python virtual environment for isolated dependencies
REM   2. Activate the virtual environment
REM   3. Upgrade pip (Python package manager)
REM   4. Install all required Python packages
REM   5. Initialize the SQLite database with sample voters
REM   6. Start the voting system application
REM -----------------------------------------------------------------------------

REM Step 1: Create Python virtual environment
python -m venv venv

REM Step 2: Activate the virtual environment
call venv\Scripts\activate

REM Step 3: Upgrade pip
python -m pip install --upgrade pip

REM Step 4: Install required packages
pip install tensorflow numpy opencv-python scikit-learn

REM Step 5: Initialize the database
python database.py

REM Step 6: Run the voting system
python voting_system.py

REM -----------------------------------------------------------------------------
REM End of script
REM -----------------------------------------------------------------------------
pause