from flask import Flask
from app.extensions import db
from app.blueprints.patients import patient_bp
from app.blueprints.doctors import doctor_bp
from app.schedular import start_scheduler

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:CK123indb#1@localhost/medicare"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    # Initialize DB
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(patient_bp, url_prefix="/patients")
    app.register_blueprint(doctor_bp, url_prefix="/doctors")


    start_scheduler(app)


    return app
