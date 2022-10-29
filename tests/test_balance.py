from urllib import response
import pytest
from rest_framework.test import APIClient
import json
client = APIClient()

@pytest.mark.django_db
def test_consolided_list_data_balance():
    users = ['test_user_1', 'test_user_2','test_user_3']
    # adding users
    for user in users:
        client.post('/add', { 'user': user })

    #adding ious
    ious = [
        {
            "lender" : "test_user_1",
            "borrower" : "test_user_3",
            "amount": 20.20,
            "expiration" : "2022-12-12 13:45:12"
        },
        {
            "lender" : "test_user_2",
            "borrower" : "test_user_1",
            "amount": 5,
            "expiration" : "2022-12-11 13:45:12"
        },
        {
            "lender" : "test_user_3",
            "borrower" : "test_user_2",
            "amount": 6.00,
            "expiration" : "2022-12-11 13:45:12"
        },
        {
            "lender" : "test_user_1",
            "borrower" : "test_user_3",
            "amount": 4,
            "expiration" : "2022-12-11 13:45:12"
        }
    ]
    for iou in ious:
        client.post('/iou', iou )

    response  = client.get('/settleup' )
    assert response.status_code == 200
    data = json.loads(response.content.decode('utf-8'))

    # comparing test results
    expected_output_test_1 = {'balance': 19.2, 'name': 'test_user_1', 'owed_by': {'test_user_3': 24.2}, 'owes': {'test_user_2': 5.0}}
    expected_output_test_2 = {'balance': -1.0, 'name': 'test_user_2', 'owed_by': {'test_user_1': 5.0}, 'owes': {'test_user_3': 6.0}}
    expected_output_test_3 = {'balance': -18.2, 'name': 'test_user_3', 'owed_by': {'test_user_2': 6.0}, 'owes': {'test_user_1': 24.2}}
    data = data.get('users')
    for debt in data:
        if debt.get('name') == 'test_user_1':
            assert expected_output_test_1 == debt
        elif debt.get('name') == 'test_user_2':
            assert expected_output_test_2 == debt
        elif debt.get('name') == 'test_user_3':
            assert expected_output_test_3 == debt
