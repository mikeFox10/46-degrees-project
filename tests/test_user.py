import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
def test_add_user():
    payload = dict(
        user = 'new user'
    )
    response = client.post('/add', payload)
    assert response.status_code == 200
    data = response.data
    print(data)
    assert len(data) == 1
    assert data['user'] == payload['user']
