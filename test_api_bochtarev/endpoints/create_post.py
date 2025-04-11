import requests
import allure
from endpoints.endpoint import Endpoint


class CreatePost(Endpoint):

    @allure.step('Создание объекта')
    def new_post(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        return self.response
