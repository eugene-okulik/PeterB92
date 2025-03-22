import pytest
import requests


@pytest.fixture(scope='session')
def start_completed():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def before_after():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def create_deleted():
    body = {"data": {"homework": "19", "fio": "BPV"}, "id": 677, "name": "test api"}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    post_id = response.json()['id']
    yield post_id
    response = requests.delete(f'http://167.172.172.115:52353/object/{post_id}')


@pytest.fixture()
def create():
    body = {"data": {"homework": "19", "fio": "BPV"}, "id": 677, "name": "test api"}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    post_id = response.json()['id']
    return post_id
