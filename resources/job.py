from flask_restful import Resource
from flask import request,abort
from marshmallow import fields, ValidationError
from data import ma,db
from models.job import Job, job_schema



class JobResource(Resource):
    def get(self, id):
        job = Job.query.get_or_404(id)
        if not job:
            abort(404, message="Could not find that id")
        return job_schema.dump(job),200

    def put(self, id):
        try:
            job = job_schema.load(request.form, partial=True)
            job.id = id
        except ValidationError as err:
            print(err.messages)
            abort(404, err.args)
        db.session.add(job)
        db.session.commit()
        return job_schema.dump(job),201

    def delete(self,id):
        # abort_non_existent_id(id)
        # del videos[id]
        return '',204

    # def patch(self,id):
        # abort_non_existent_id(id)
        # try:
        #     video = videoSchema.load(request.form)


