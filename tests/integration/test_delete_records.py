import requests

BASE = "http://127.0.0.1:5000"

def test_delete_record():
    response = requests.delete(BASE+"/job/"+str(1))
    assert response.status_code == 204
    assert response.text == ''