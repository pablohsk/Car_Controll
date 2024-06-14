import pytest

def test_register_user(client):
    response = client.post('/users/register', json={'username': 'newuser', 'password': 'newpass'})
    assert response.status_code == 201
    assert response.json['message'] == 'User created successfully'

def test_register_user_existing_username(client):
    response = client.post('/users/register', json={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 400
    assert response.json['error'] == 'User already exists'

def test_login_user(client):
    response = client.post('/users/login', json={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_login_user_invalid_credentials(client):
    response = client.post('/users/login', json={'username': 'testuser', 'password': 'wrongpass'})
    assert response.status_code == 401
    assert response.json['error'] == 'Invalid credentials'
