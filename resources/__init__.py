from resources.job import JobResource

def add_resource(api):
    api.add_resource(JobResource, "/job/<int:id>")