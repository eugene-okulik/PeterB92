import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    headers = {"Content-Type": "application/json"}

    @allure.step('Проверка статус кода ответа')
    def check_response_status_code_is_correct(self, response):
        assert self.response.status_code == 200
