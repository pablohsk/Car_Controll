import pytest
from app import create_app, db
from app.config_test import Config

@pytest.fixture(scope='module')
def app():
    app = create_app(Config)
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    client = app.test_client()

    user_response = client.post('/users/register', json={'username': 'testuser', 'password': 'testpass'})
    assert user_response.status_code == 201
    
    login_response = client.post('/users/login', json={'username': 'testuser', 'password': 'testpass'})
    assert login_response.status_code == 200
    
    access_token = login_response.json['access_token']
    client.environ_base['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
    
    return client
