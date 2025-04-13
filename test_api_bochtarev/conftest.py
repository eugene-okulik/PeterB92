import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.patch_object import PatchObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


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
def create_deleted(create_object_endpoint, delete_object_endpoint):
    body = {"data": {"homework": "19", "fio": "BPV"}, "id": 677, "name": "test api"}
    response = create_object_endpoint.new_object(body)
    object_id = response.json()['id']
    yield object_id
    response = delete_object_endpoint.delete_object(object_id)


@pytest.fixture()
def create(create_object_endpoint):
    body = {"data": {"homework": "19", "fio": "BPV"}, "id": 677, "name": "test api"}
    response = create_object_endpoint.new_object(body)
    object_id = response.json()['id']
    return object_id
