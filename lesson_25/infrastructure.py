import requests

url = "https://api.restful-api.dev/"

url2 = "https://reqres.in/api/"


def get_an_object(object_id):
    response = requests.get(f"{url}objects/{object_id}")
    return response


def create_an_object(dictionary):
    response = requests.post("https://api.restful-api.dev/objects", json=dictionary)
    return response


def login():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(f'{url2}login', json=body)
    return response


def create_user(token):
    headers = {"content-type": "application/json",
               'token': token}
    return requests.post(f'{url2}users', json={
        "name": "morpheus",
        "job": "leader"
    }, headers=headers)
