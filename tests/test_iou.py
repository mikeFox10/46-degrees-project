import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
def test_fail_adding_iou():
    # fail when ammount is negative or 0
    payload1 = dict(
        user = 'test_user_1'
    )
    payload2 = dict(
        user = 'test_user_2'
    )
    response = client.post('/add', payload1)
    response = client.post('/add', payload2)


    payload_iou = {
        "lender" : "test_user_1",
        "borrower" : "test_user_2",
        "amount": -4,
        "expiration" : "2022-12-11 13:45:12"
    }
    response = client.post('/iou', payload_iou)

    assert response.status_code == 400


@pytest.mark.django_db
def test_fail_adding_iou():
    # fail when ammount is negative or 0
    payload1 = dict(
        user = 'test_user_1'
    )
    payload2 = dict(
        user = 'test_user_2'
    )
    response = client.post('/add', payload1)
    response = client.post('/add', payload2)


    payload_iou = {
        "lender" : "test_user_1",
        "borrower" : "test_user_2",
        "amount": 433.00,
        "expiration" : "2022-12-11 13:45:12"
    }
    response = client.post('/iou', payload_iou)

    assert response.status_code == 200
