import pytest
import requests
from endpoints.create_post import CreatePost
from endpoints.update_post import UpdatePost
from endpoints.patch_post import PatchPost
from endpoints.delete_post import DeletePost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def patch_post_endpoint():
    return PatchPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


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
