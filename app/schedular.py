from apscheduler.schedulers.background import BackgroundScheduler
from app.utils.excel_reader import read_patients_excel, read_doctors_excel
from app.models import Patient, Doctor
from app.extensions import db

def import_patients_job(app):
    with app.app_context():
        df = read_patients_excel("/Users/arshabk/Documents/arsha/Workspace/Medicare/medicare_data/PatientDetails.xlsx")

        for _, row in df.iterrows():
            patient = Patient(
                patientUsername=row["patientusername"],
                patientPassword=row["patientpassword"]
            )
            db.session.add(patient)

        db.session.commit()
        print("Patients imported (scheduler).")

def import_doctors_job(app):
    with app.app_context():
        df = read_doctors_excel("/Users/arshabk/Documents/arsha/Workspace/Medicare/medicare_data/DoctorDetails.xlsx")

        for _, row in df.iterrows():
            doctor = Doctor(
                doctorName=row["doctorname"],
                type=row["type"],
                location=row["location"],
                date=row["date"],
                fee=row["fee"]
            )
            db.session.add(doctor)

        db.session.commit()
        print("Doctors imported (scheduler).")

def start_scheduler(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: import_patients_job(app), "interval", days=1)
    scheduler.add_job(lambda: import_doctors_job(app), "interval", days=1)
    scheduler.start()
