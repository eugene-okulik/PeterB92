import requests
import allure
from endpoints.endpoint import Endpoint


class PatchObject(Endpoint):

    @allure.step('Обновление объекта')
    def patch_object(self, create_deleted, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{create_deleted}',
            json=body,
            headers=headers
        )
        return self.response
