import requests
import allure
from endpoints.endpoint import Endpoint


class PatchPost(Endpoint):

    @allure.step('Обновление объекта')
    def patch_post(self, create_deleted, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{create_deleted}',
            json=body,
            headers=headers
        )
        return self.response
