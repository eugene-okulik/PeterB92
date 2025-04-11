import pytest
import allure

TEST_DATA = [
    {"data": {"homework": "21", "fio1": "BPV1"}, "name": 'name1'},
    {"data": {"homework": "21", "fio2": "BPV2"}, "name": 'name2'}
]


@allure.title('Создание объекта')
@allure.feature('Создание')
@pytest.mark.critical
@pytest.mark.parametrize('data', TEST_DATA)
def test_create_object(create_post_endpoint, before_after, start_completed, data):
    response = create_post_endpoint.new_post(body=data)
    create_post_endpoint.check_response_status_code_is_correct(response)


@allure.title('Редактирование объекта через PUT')
@allure.feature('Изменение')
@allure.story('Put')
@pytest.mark.medium
def test_change_object_put(update_post_endpoint, before_after, create):
    body = {"data": {"homework": "19", "fio": "BPV2"}, "name": "test api change_object"}
    response = update_post_endpoint.update_post(create, body)
    update_post_endpoint.check_response_status_code_is_correct(response)


@allure.title('Редактирование объекта через patch')
@allure.feature('Изменение')
@allure.story('patch')
def test_change_object_patch(patch_post_endpoint, before_after, create_deleted):
    body = {"name": "test api change_object_patch"}
    response = patch_post_endpoint.patch_post(create_deleted, body)
    patch_post_endpoint.check_response_status_code_is_correct(response)


@allure.description('Проверяется корректность удаления объекта')
@allure.title('Удаление объекта')
@allure.feature('Удаление')
def test_delete_object(delete_post_endpoint, before_after, create):
    response = delete_post_endpoint.delete_post(create)
    delete_post_endpoint.check_response_status_code_is_correct(response)
