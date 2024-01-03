import requests

def test_health_endpoint(app_client):
    client, app_url = app_client
    response = requests.get(f"{app_url}/health")
    data = response.json()

    assert not app_url is None
    assert response.status_code == 200
    assert data['data']['status'] == 'OK'


def test_health_check(app_client):
    client, app_url = app_client
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status_code": 200,
        "data": {
            "status": "OK",
        }
    }