# Medical Data Management System

A simple command-line based medical data management system written in Python that helps manage patient records, medical history, and appointments.

## Features

- Add new patients with basic information
- View patient information
- Add medical records with diagnosis and prescriptions
- Schedule appointments
- View medical history
- View appointments
- Data persistence using JSON storage

## Requirements

- Python 3.6 or higher
- Required packages (install using `pip install -r requirements.txt`):
  - tabulate
  - python-dateutil

## Installation

1. Clone or download this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```
   python medical_system.py
   ```

2. Follow the menu options:
   - Option 1: Add a new patient
   - Option 2: View patient information
   - Option 3: Add medical record
   - Option 4: Schedule appointment
   - Option 5: View medical history
   - Option 6: View appointments
   - Option 7: Exit

## Data Storage

All patient data is stored in a `medical_data.json` file in the same directory as the program. The data is automatically saved after each modification and loaded when the program starts.

## Note

This is a basic implementation and should be enhanced with proper security measures and additional features before using in a production environment. 