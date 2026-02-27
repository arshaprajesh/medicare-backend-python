# medicare-backend-python

It is a Flask‑based backend service that automatically imports **Patients** and **Doctors** from Excel files into a MySQL database. The system supports both **manual imports via API routes** and **automated hourly imports** using APScheduler. It is designed for healthcare-style data ingestion pipelines where Excel is the primary data source. 

Project Structure
<img width="291" height="389" alt="image" src="https://github.com/user-attachments/assets/f4e601c5-442d-420a-83b8-e7611ec484b0" />

Requirements

Python 3.9+
Flask
SQLAlchemy
PyMySQL
Pandas
APScheduler
MySQL
postman

 How the System Works

### 1. Excel Reader Utilities
Located in `app/utils/excel_reader.py`, these functions load Excel files, normalize column names, and return a clean DataFrame.

### 2. Manual Import Routes
Two API endpoints allow manual imports:

- `POST /patients/import-all`
- `POST /doctors/import-all`

Each route:
- Reads the Excel file
- Cleans NaN/NaT rows
- Parses dates safely
- Inserts valid rows into MySQL

### 3. Automated Hourly Scheduler
The scheduler runs inside `app/scheduler.py` and is started in `create_app()`.

It:
- Loads Excel files every hour
- Cleans invalid rows
- Inserts new records into the database
- Logs each run

  Setup Instructions

  1. Clone the repository
     https://github.com/arshaprajesh/medicare-backend-python.git
     
  2. Create and activate a virtual environment
     python3 -m venv venv
     source venv/bin/activate

  3. Install dependencies
     pip install -r requirements.txt

  4. Configure MySQL connection
     app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@localhost/medicare"

  5. Run the application
     python3 app.py
You should see:
Scheduler started...


API Endpoints
Import all patients
POST /patients/import-all

Import all doctors
POST /doctors/import-all

Both endpoints return:
{
  "message": "All patients inserted successfully"
}


Scheduler Details
The scheduler runs every hour:

scheduler.add_job(lambda: import_doctors_job(app), "interval", hours=1) 
scheduler.add_job(lambda: import_patients_job(app), "interval", hours=1)

To test quickly, change to:
seconds=5


Data Cleaning Logic
Before inserting into MySQL, the system:

Removes fully empty rows (dropna(how="all"))
Removes rows missing required fields (dropna(subset=[...]))
Converts dates safely (pd.to_datetime(..., errors="coerce"))
Skips invalid rows

This prevents MySQL errors like:

nan can not be used with MySQL
Incorrect date value: 'NaT'

