from app.extensions import ma
from app.models import Doctor

class DoctorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Doctor
        load_instance = True

doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)
