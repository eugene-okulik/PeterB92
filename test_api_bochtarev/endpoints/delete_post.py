import requests
import allure
from endpoints.endpoint import Endpoint


class DeletePost(Endpoint):

    @allure.step('Удаление объекта')
    def delete_post(self, create, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/{create}')
        return self.response
