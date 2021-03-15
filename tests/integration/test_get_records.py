import requests

BASE = "http://127.0.0.1:5000"

def test_get_record():
    response = requests.get(BASE+"/job/"+str(1))
    assert response.status_code == 200
    assert response.json()  == {"id": 1, "name": "job1","created_at" : '2015-06-05T08:10:10.000010',"status" : "started"}

def test_get_missing_record():
    response = requests.get(BASE+"/job/"+str(10))
    assert response.status_code == 404
    assert response.json() == {"message":"Could not find that id"}