import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_recommendations(client):
    response = client.post('/api/recommendations', json={
        "username": "user123",
        "category_id": 1,
        "mood": "happy"
    })
    assert response.status_code == 200
    assert isinstance(response.json, list)
