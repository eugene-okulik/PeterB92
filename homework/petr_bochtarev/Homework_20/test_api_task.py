import requests
import pytest
import allure


@allure.title('Создание объекта')
@allure.feature('Создание')
@pytest.mark.critical
@pytest.mark.parametrize('number_id', [417, 418, 419])
def test_create_object(before_after, start_completed, number_id):
    body = {"data": {"homework": "18", "fio": "BPV"}, "id": number_id, "name": "test api"}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    assert response.status_code == 200


@allure.title('Редактирование объекта через PUT')
@allure.feature('Изменение')
@allure.story('Put')
@pytest.mark.medium
def test_change_object_put(before_after, create_deleted):
    body = {"data": {"homework": "19", "fio": "BPV2"}, "id": 677, "name": "test api change_object"}
    headers = {"Content-Type": "application/json"}
    response = requests.put(f'http://167.172.172.115:52353/object/{create_deleted}', json=body, headers=headers)
    assert response.status_code == 200


@allure.title('Редактирование объекта через patch')
@allure.feature('Изменение')
@allure.story('patch')
def test_change_object_patch(before_after, create_deleted):
    body = {"name": "test api change_object_patch"}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(f'http://167.172.172.115:52353/object/{create_deleted}', json=body, headers=headers)
    assert response.status_code == 300


@allure.description('Проверяется корректность удаления объекта')
@allure.title('Удаление объекта')
@allure.feature('Удаление')
def test_delete_object(before_after, create):
    with allure.step('Удаление объекта'):
        response = requests.delete(f'http://167.172.172.115:52353/object/{create}')
    with allure.step('Проверка статус-кода, должен равняться 400'):
        assert response.status_code == 400
