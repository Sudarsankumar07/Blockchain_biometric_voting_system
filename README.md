# Blockchain Biometric Voting System

This project is a secure electronic voting system using blockchain concepts and fingerprint-based biometric authentication.

## How to Run (Windows)

### 1. Using the Provided Script

A Windows batch script (`run.sh`) is provided to automate setup and execution.

#### What the Script Does

- **Creates a Python virtual environment** to isolate dependencies.
- **Activates the virtual environment** so installed packages do not affect your system Python.
- **Upgrades pip** to the latest version.
- **Installs all required Python packages** (`tensorflow`, `numpy`, `opencv-python`, `scikit-learn`).
- **Initializes the database** by running `database.py`.
- **Starts the voting system** by running `voting_system.py`.

#### Steps

1. Open **Command Prompt** and navigate to your project folder.
2. Run:
   ```
   run.sh
   ```
   or, if you saved it as a `.bat` file (recommended for Windows):
   ```
   run.bat
   ```

   > If you see a security warning, right-click the file and select "Run as administrator".

### 2. Manual Steps (if you prefer)

1. **Create and activate a virtual environment:**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Upgrade pip and install dependencies:**
   ```
   python -m pip install --upgrade pip
   pip install tensorflow numpy opencv-python scikit-learn
   ```

3. **Initialize the database:**
   ```
   python database.py
   ```

4. **Run the voting system:**
   ```
   python voting_system.py
   ```

---

**Note:**  
- Place all fingerprint images in the `fingerprint_database` folder before running the system.
- The script pauses at the end so you can see any output or errors.

---
```# Blockchain Biometric Voting System

This project is a secure electronic voting system using blockchain concepts and fingerprint-based biometric authentication.

## How to Run (Windows)

### 1. Using the Provided Script

A Windows batch script (`run.sh`) is provided to automate setup and execution.

#### What the Script Does

- **Creates a Python virtual environment** to isolate dependencies.
- **Activates the virtual environment** so installed packages do not affect your system Python.
- **Upgrades pip** to the latest version.
- **Installs all required Python packages** (`tensorflow`, `numpy`, `opencv-python`, `scikit-learn`).
- **Initializes the database** by running `database.py`.
- **Starts the voting system** by running `voting_system.py`.

#### Steps

1. Open **Command Prompt** and navigate to your project folder.
2. Run:
   ```
   run.sh
   ```
   or, if you saved it as a `.bat` file (recommended for Windows):
   ```
   run.bat
   ```

   > If you see a security warning, right-click the file and select "Run as administrator".

### 2. Manual Steps (if you prefer)

1. **Create and activate a virtual environment:**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Upgrade pip and install dependencies:**
   ```
   python -m pip install --upgrade pip
   pip install tensorflow numpy opencv-python scikit-learn
   ```

3. **Initialize the database:**
   ```
   python database.py
   ```

4. **Run the voting system:**
   ```
   python voting_system.py
   ```

---

**Note:**  
- Place all fingerprint images in the `fingerprint_database` folder before running the system.
- The script pauses at the end so you can see any output or errors.

---