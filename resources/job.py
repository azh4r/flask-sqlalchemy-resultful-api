from flask_restful import Resource
from flask import request,abort, Response
from marshmallow import fields, ValidationError
from data import ma,db
from models.job import Job, job_schema



class JobResource(Resource):
    # get the resource given the id
    def get(self, id):
        job = Job.query.filter(Job.id == id).first()
        if not job:
            abort(404, description="Could not find that id")
        return job_schema.dump(job),200



    # Check if a resource exists.  If not create it.
    # In REST PUT can also be used to update an existing resource
    # And the URL must contain the resource id
    def put(self, id):
        job = Job.query.filter(Job.id == id).first()
        if job:
            abort(404, description="Id already exists, cannot add")
        try:
            job = job_schema.load(request.form, partial=True)
            job.id = id
        except ValidationError as err:
            print(err.messages)
            abort(404, err.messages)
        db.session.add(job)
        db.session.commit()
        return job_schema.dump(job),201

    # Update an existing resource with new data
    def patch(self, id):
        job = Job.query.filter(Job.id == id).first()
        if not job:
            abort(404, message = "Id does not exist, cannot modify")
        try:
            job_update = job_schema.load(request.form, partial=True)
        except ValidationError as err:
            abort(404, err.messages)
        if job_update.created_at:
            job.created_at = job_update.created_at
        if job_update.status:
            job.status = job_update.status
        if job_update.name:
            job.name = job_update.name
        db.session.commit()
        return job_schema.dump(job),200

    # delete an existing resource
    def delete(self,id):
        job = Job.query.filter(Job.id == id).first()
        if not job:
            abort(404, message = "id does not exist, cannot delete")
        db.session.delete(job)
        db.session.commit()
        return Response(status = 204)

    

class JobPostResource(Resource):
    # POST is to create a new resource, whether it already exists or not.
    # the URL will not contain the resource id
    def post(self):
        try:
            job = job_schema.load(request.form, partial=True)
            print('loaded')
        except ValidationError as err:
            print(err.messages)
            abort(404,err.messages)

        db.session.add(job)
        db.session.commit()
        return job_schema.dump(job), 201