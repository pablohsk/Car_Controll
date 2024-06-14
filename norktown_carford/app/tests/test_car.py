import pytest
from app import create_app, db
from app.models.owner import Owner
from app.models.car import Car

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_car(client):
    owner_response = client.post('/owners', json={'name': 'John Doe'})
    owner_id = owner_response.json['id']
    car_response = client.post('/cars', json={'color': 'blue', 'model': 'sedan', 'owner_id': owner_id})
    assert car_response.status_code == 201
    assert car_response.json['color'] == 'blue'
    assert car_response.json['model'] == 'sedan'
    assert car_response.json['owner_id'] == owner_id

def test_create_car_limit(client):
    owner_response = client.post('/owners', json={'name': 'John Doe'})
    owner_id = owner_response.json['id']
    for i in range(3):
        car_response = client.post('/cars', json={'color': 'blue', 'model': 'sedan', 'owner_id': owner_id})
        assert car_response.status_code == 201
    car_response = client.post('/cars', json={'color': 'blue', 'model': 'sedan', 'owner_id': owner_id})
    assert car_response.status_code == 400
    assert car_response.json['error'] == 'Owner not found or car limit reached'
