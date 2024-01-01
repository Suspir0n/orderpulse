import requests
from app.tests.happy_path import env_app_url, client

def test_health_endpoint():
    app_url = env_app_url
    response = requests.get(f"{app_url}/health")
    data = response.json()

    assert not app_url is None
    assert response.status_code == 200
    assert data['data']['status'] == 'OK'


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status_code": 200,
        "data": {
            "status": "OK",
        }
    }