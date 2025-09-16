# Blockchain Biometric Voting System

This project implements a secure electronic voting system using blockchain concepts and fingerprint-based biometric authentication.

---

## Project Files Overview

- **run.bat**  
  Automates environment setup, dependency installation, database initialization, and launches the voting system on Windows.

- **database.py**  
  Handles voter registration, blockchain-style hashing, and sets up the SQLite database.

- **fingerprint_Matching.py**  
  Uses deep learning (MobileNetV2) to extract fingerprint features and match fingerprints for biometric authentication.

- **voting_system.py**  
  Main application logic: verifies voters, manages voting, and displays results.

- **voter_blockchain.db**  
  SQLite database file created automatically to store voter and voting data.

- **fingerprint_database/**  
  Folder containing registered fingerprint images for biometric verification.

---

## Quick Start (Windows)

A batch script (`run.bat`) is provided to automate the setup and execution process.

### What `run.bat` Does

- Creates a Python virtual environment (`venv`) for isolated dependencies.
- Activates the virtual environment.
- Upgrades `pip` to the latest version.
- Installs all required Python packages (`tensorflow`, `numpy`, `opencv-python`, `scikit-learn`).
- Initializes the database by running `database.py`.
- Starts the voting system by running `voting_system.py`.

### How to Use

1. **Place all fingerprint images** in the `fingerprint_database` folder.
2. **Open Command Prompt** and navigate to your project directory:
   ```
   cd C:\Users\sudarsan kumar\Blockchain_biometric_voting_system
   ```
3. **Run the batch file:**
   ```
   run.bat
   ```
4. **Follow the on-screen prompts** to complete the setup and voting process.

> The script will pause at the end so you can review any output or errors.

---

## Manual Setup (Alternative)

If you prefer to run steps manually:

1. Create and activate the virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
2. Upgrade pip and install dependencies:
   ```
   python -m pip install --upgrade pip
   pip install tensorflow numpy opencv-python scikit-learn
   ```
3. Initialize the database:
   ```
   python database.py
   ```
4. Run the voting system:
   ```
   python voting_system.py
   ```

---

## Notes

- Only registered voters who have not voted can cast a vote.
- Fingerprint matching uses deep learning and may require a compatible system.
- You can modify the database schema or add more candidates as needed.

---