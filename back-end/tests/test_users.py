import json
from models import User

def test_register_user(test_client):
    user_data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    }
    response = test_client.post('/register', json=user_data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['user']['username'] == 'testuser'

def test_login_user(test_client):
    login_data = {
        'email': 'testuser@example.com',
        'password': 'password123'
    }
    response = test_client.post('/login', json=login_data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Login successful'
