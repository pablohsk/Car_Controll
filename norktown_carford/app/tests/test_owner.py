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

def test_create_owner(client):
    response = client.post('/owners', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert response.json['name'] == 'John Doe'

def test_delete_owner_with_car(client):
    owner_response = client.post('/owners', json={'name': 'Jane Doe'})
    owner_id = owner_response.json['id']

    car_response = client.post('/cars', json={'color': 'blue', 'model': 'sedan', 'owner_id': owner_id})
    assert car_response.status_code == 201

    delete_response = client.delete(f'/owners/{owner_id}')
    assert delete_response.status_code == 400
    assert delete_response.json['error'] == 'Esse usuário ainda possui um carro associado a ele'

def test_delete_owner_without_car(client):
    owner_response = client.post('/owners', json={'name': 'Jane Doe'})
    owner_id = owner_response.json['id']

    delete_response = client.delete(f'/owners/{owner_id}')
    assert delete_response.status_code == 200
    assert delete_response.json['message'] == 'Proprietário deletado com sucesso'
