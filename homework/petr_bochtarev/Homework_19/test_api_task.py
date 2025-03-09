import requests
import pytest


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


@pytest.mark.critical
@pytest.mark.parametrize('number_id', [417, 418, 419])
def test_create_object(before_after, start_completed, number_id):
    body = {"data": {"homework": "18", "fio": "BPV"}, "id": number_id, "name": "test api"}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    assert response.status_code == 200


@pytest.mark.medium
def test_change_object_put(before_after, create_deleted):
    body = {"data": {"homework": "19", "fio": "BPV2"}, "id": 677, "name": "test api change_object"}
    headers = {"Content-Type": "application/json"}
    response = requests.put(f'http://167.172.172.115:52353/object/{create_deleted}', json=body, headers=headers)
    assert response.status_code == 200


def test_change_object_patch(before_after, create_deleted):
    body = {"name": "test api change_object_patch"}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(f'http://167.172.172.115:52353/object/{create_deleted}', json=body, headers=headers)
    assert response.status_code == 200


def test_delete_object(before_after, create):
    response = requests.delete(f'http://167.172.172.115:52353/object/{create}')
    assert response.status_code == 200
