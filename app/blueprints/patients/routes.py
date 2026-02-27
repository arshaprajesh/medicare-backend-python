from flask import Blueprint, jsonify
from app.models import Patient
from app.utils import read_patients_excel
from app.extensions import db
import pandas as pd

patient_bp = Blueprint("patient_bp", __name__)

@patient_bp.route("/import-all", methods=["POST"])
def import_all_patients():

    df = read_patients_excel("/Users/arshabk/Documents/arsha/Workspace/Medicare/medicare_data/PatientDetails.xlsx")

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()
    print("Columns:", df.columns)

    # Remove fully empty rows
    df = df.dropna(how="all")

    # Remove rows missing required fields
    df = df.dropna(subset=["patientusername", "patientpassword"], how="any")

    # Iterate list of patients one by one
    for index, row in df.iterrows():

        patient = Patient(
            patientUsername=row["patientusername"],
            patientPassword=row["patientpassword"]
        )
        db.session.add(patient)

    # Commit after all inserts
    db.session.commit()

    return jsonify({"message": "All patients inserted successfully"}), 201
