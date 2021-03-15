from resources.job import JobResource, JobPostResource

def add_resource(api):
    api.add_resource(JobResource, "/job/<int:id>")
    api.add_resource(JobPostResource, "/job")