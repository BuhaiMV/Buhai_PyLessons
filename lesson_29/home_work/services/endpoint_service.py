import requests


class Endpoint:
    def __init__(self):
        self.url = 'https://api.restful-api.dev/objects'

    def get_request(self, data_id):
        response = requests.get(f"{self.url}/{data_id}")
        return response.json()

    def post_request(self, body):
        response = requests.post(f"{self.url}", json=body)
        return response.json()

    def put_request(self, data_id, body):
        response = requests.put(f"{self.url}/{data_id}", json=body)
        return response.json()
