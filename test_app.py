import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


# 1. Test home endpoint
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200


# 2. Test home content
def test_home_content(client):
    response = client.get('/')
    data = response.get_json()
    assert "message" in data


# 3. Test users endpoint
def test_users(client):
    response = client.get('/users')
    assert response.status_code == 200


# 4. Test users data format
def test_users_data(client):
    response = client.get('/users')
    data = response.get_json()
    assert isinstance(data, list)


# 5. Test users length
def test_users_length(client):
    response = client.get('/users')
    data = response.get_json()
    assert len(data) > 0


# 6. Test health endpoint
def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200


# 7. Test health response
def test_health_response(client):
    response = client.get('/health')
    data = response.get_json()
    assert data["status"] == "OK"


# 8. Test invalid route
def test_invalid_route(client):
    response = client.get('/invalid')
    assert response.status_code == 404
