import pytest

def test_create_car(client):
    owner_response = client.post('/owners', json={'name': 'John Doe'})
    assert owner_response.status_code == 201
    owner_id = owner_response.json['id']

    car_response = client.post('/cars', json={'color': 'blue', 'model': 'sedan', 'owner_id': owner_id})
    assert car_response.status_code == 201
    assert car_response.json['color'] == 'blue'
    assert car_response.json['model'] == 'sedan'
    assert car_response.json['owner_id'] == owner_id

def test_create_car_owner_not_found(client):
    car_response = client.post('/cars', json={'color': 'blue', 'model': 'sedan', 'owner_id': 999})
    assert car_response.status_code == 400
    assert car_response.json['error'] == 'Owner not found or car limit reached'

def test_create_car_limit(client):
    owner_response = client.post('/owners', json={'name': 'John Doe'})
    assert owner_response.status_code == 201
    owner_id = owner_response.json['id']

    for _ in range(3):
        car_response = client.post('/cars', json={'color': 'blue', 'model': 'sedan', 'owner_id': owner_id})
        assert car_response.status_code == 201

    car_response = client.post('/cars', json={'color': 'blue', 'model': 'sedan', 'owner_id': owner_id})
    assert car_response.status_code == 400
    assert car_response.json['error'] == 'Owner not found or car limit reached'

def test_get_car(client):
    owner_response = client.post('/owners', json={'name': 'John Doe'})
    assert owner_response.status_code == 201
    owner_id = owner_response.json['id']

    car_response = client.post('/cars', json={'color': 'blue', 'model': 'sedan', 'owner_id': owner_id})
    assert car_response.status_code == 201
    car_id = car_response.json['id']

    get_response = client.get(f'/cars/{car_id}')
    assert get_response.status_code == 200
    assert get_response.json['color'] == 'blue'
    assert get_response.json['model'] == 'sedan'
    assert get_response.json['owner_id'] == owner_id

def test_update_car(client):
    owner_response = client.post('/owners', json={'name': 'John Doe'})
    assert owner_response.status_code == 201
    owner_id = owner_response.json['id']

    car_response = client.post('/cars', json={'color': 'blue', 'model': 'sedan', 'owner_id': owner_id})
    assert car_response.status_code == 201
    car_id = car_response.json['id']

    update_response = client.put(f'/cars/{car_id}', json={'color': 'red'})
    assert update_response.status_code == 200
    assert update_response.json['color'] == 'red'
    assert update_response.json['model'] == 'sedan'

def test_delete_car(client):
    owner_response = client.post('/owners', json={'name': 'John Doe'})
    assert owner_response.status_code == 201
    owner_id = owner_response.json['id']

    car_response = client.post('/cars', json={'color': 'blue', 'model': 'sedan', 'owner_id': owner_id})
    assert car_response.status_code == 201
    car_id = car_response.json['id']

    delete_response = client.delete(f'/cars/{car_id}')
    assert delete_response.status_code == 200
    assert delete_response.json['message'] == 'Car deleted'
