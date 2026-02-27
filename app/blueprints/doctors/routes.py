from flask import Blueprint, jsonify

from app.extensions import db
from app.models import Doctor
from app.utils import read_doctors_excel
import pandas as pd

doctor_bp = Blueprint("doctor_bp", __name__)

@doctor_bp.route("/import-all", methods=["POST"])
def import_all_doctors():

    df = read_doctors_excel("/Users/arshabk/Documents/arsha/Workspace/Medicare/medicare_data/DoctorDetails.xlsx")

    # Remove fully empty rows
    df = df.dropna(how="all")

    for index, row in df.iterrows():

        # Convert date safely
        date_value = pd.to_datetime(row["date"], errors="coerce")
        if pd.isna(date_value):
            continue # skip invalid dates

        doctor = Doctor(
            doctorName=row["doctorname"],
            type=row["type"],
            location=row["location"],
            date=date_value.date(),
            fee=row["fee"]
        )

        db.session.add(doctor)

    db.session.commit()

    return jsonify({"message": "All doctors inserted successfully"}), 201
