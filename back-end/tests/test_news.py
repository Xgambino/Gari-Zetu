import json
from models import News

def test_get_news(test_client):
    response = test_client.get('/news')
    assert response.status_code == 200
    assert isinstance(json.loads(response.data), list)

# tests/test_news.py
# def test_post_news(client):
#     response = client.post('/news', json={
#         'image_url': 'https://example.com/news.jpg',
#         'description': 'New Event',
#         'location': 'Nairobi',
#         'ticket_price': 'KES 3,000',
#         'date': '2024-08-15'  
#     })
#     assert response.status_code == 201
#     data = response.json
#     assert 'id' in data
#     assert data['description'] == 'New Event'