from locust import task, HttpUser
import random


class ObjectInfo(HttpUser):

    @task(3)
    def get_one_object(self):
        self.client.get(f'/object/{random.choice([1, 5488, 5501, 5565])}')

    @task(1)
    def get_all_object(self):
        self.client.get('/object')
