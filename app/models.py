from app.extensions import db

class Patient(db.Model):
    __tablename__ ="patients"

    id = db.Column(db.Integer, primary_key=True)
    patientUsername = db.Column(db.String(120),nullable=False)
    patientPassword = db.Column(db.String(120),nullable=False)


class Doctor(db.Model):
    __tablename__ ="doctors"
    id = db.Column(db.Integer, primary_key=True)
    doctorName = db.Column(db.String(120),nullable=False)
    type = db.Column(db.String(120),nullable=False)
    location = db.Column(db.String(120),nullable=False)
    date = db.Column(db.Date, nullable=False)
    fee = db.Column(db.Integer,nullable=False)




