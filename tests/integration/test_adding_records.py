import requests
from datetime import datetime

BASE = "http://127.0.0.1:5000/"

def test_put_record():
    data = [{"name": "job1","created_at" : datetime(2015, 6, 5, 8, 10, 10, 10),"status" : "started"}, 
    {"name": "job2","created_at" : datetime(2015, 6, 5, 8, 10, 10, 10), "status" : "pending"}, 
    {"name": "job3","created_at" : datetime(2015, 6, 5, 8, 10, 10, 10), "status" : "finished"}]
    response = requests.put(BASE+ "job/"+str(1), {"name": "job1","created_at" : datetime(2015, 6, 5, 8, 10, 10, 10),"status" : "started"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "job1","created_at" : '2015-06-05T08:10:10.000010',"status" : "started"}