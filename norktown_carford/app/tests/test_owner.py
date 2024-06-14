import pytest

def test_create_owner(client):
    response = client.post('/owners', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert response.json['name'] == 'John Doe'

def test_get_owner(client):
    response = client.post('/owners', json={'name': 'John Doe'})
    assert response.status_code == 201
    owner_id = response.json['id']

    get_response = client.get(f'/owners/{owner_id}')
    assert get_response.status_code == 200
    assert get_response.json['name'] == 'John Doe'

def test_update_owner(client):
    response = client.post('/owners', json={'name': 'John Doe'})
    assert response.status_code == 201
    owner_id = response.json['id']

    update_response = client.put(f'/owners/{owner_id}', json={'name': 'Jane Doe'})
    assert update_response.status_code == 200
    assert update_response.json['name'] == 'Jane Doe'

def test_delete_owner_with_car(client):
    owner_response = client.post('/owners', json={'name': 'Jane Doe'})
    assert owner_response.status_code == 201
    owner_id = owner_response.json['id']

    car_response = client.post('/cars', json={'color': 'blue', 'model': 'sedan', 'owner_id': owner_id})
    assert car_response.status_code == 201

    delete_response = client.delete(f'/owners/{owner_id}')
    assert delete_response.status_code == 400
    assert delete_response.json['error'] == 'Não foi possível deletar owner pois ainda há carros no seu nome'

def test_delete_owner_without_car(client):
    owner_response = client.post('/owners', json={'name': 'Jane Doe'})
    assert owner_response.status_code == 201
    owner_id = owner_response.json['id']

    delete_response = client.delete(f'/owners/{owner_id}')
    assert delete_response.status_code == 200
    assert delete_response.json['message'] == 'Owner deletado com sucesso'
