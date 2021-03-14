from data import db, ma
from datetime import datetime

class Job(db.Model):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    created_at = db.Column(db.DateTime, nullable = False)
    status = db.Column(db.String(10), nullable = False)

    def __repr__(self):
        return f"Job(name = {name}, created_at = {created_at}, status= {status})"

class JobSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Job
        load_instance = True

job_schema = JobSchema()
jobs_schema = JobSchema(many=True)

