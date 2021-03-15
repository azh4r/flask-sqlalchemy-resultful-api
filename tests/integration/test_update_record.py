import requests

BASE = "http://127.0.0.1:5000"

def test_update_record():
    response = requests.patch(BASE+"/job/"+str(1),{"status" : "pending"})
    assert response.status_code == 200
    assert response.json()  == {"id": 1, "name": "job1","created_at" : '2015-06-05T08:10:10.000010',"status" : "pending"}

