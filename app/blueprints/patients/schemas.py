from app.extensions import ma
from app.models import Patient

class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient
        load_instance = True

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)
