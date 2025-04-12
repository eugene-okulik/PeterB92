import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step('Обновление объекта')
    def update_object(self, create, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{create}',
            json=body,
            headers=headers
        )
        return self.response
