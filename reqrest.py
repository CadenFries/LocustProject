import random

from locust import HttpUser, constant, task


class RecRequest(HttpUser):
    host = 'https://reqres.in'
    wait_time = constant(1)

    @task
    def get_users(self):
        res = self.client.get(f'/api/users?page={random.randint(1,5)}')
        print(res.text)
        print(res.status_code)
        print(res.headers)

    @task
    def create_user(self):
        res = self.client.post('/api/users', data='''{"name":"caden","job":"leader"}''')
        print(res.text)
        print(res.status_code)
        print(res.headers)