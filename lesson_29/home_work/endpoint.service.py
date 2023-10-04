import requests


class Endpoint:

    def get_request(self, url):
        response = requests.get(url)
        return response.json()

    def post_request(self, url, body):
        response = requests.post(url, json=body)
        return response.json()

    def put_request(self, url, body):
        response = requests.put(url, json=body)
        return response.json()
