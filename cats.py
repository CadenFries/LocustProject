import random
from locust import HttpUser, TaskSet, constant, task


class CatRequests(TaskSet):

    @task
    def get_random_status(self):
        status_code = str(random.randint(100, 600))
        url = '/' + status_code
        print(f'Getting status {status_code}')
        self.client.get(url)


class LoadTest(HttpUser):
    host = 'https://http.cat'
    wait_time = constant(1)
    tasks = [CatRequests]
