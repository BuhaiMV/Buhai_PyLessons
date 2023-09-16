import requests

url = "https://api.restful-api.dev/"


def get_an_object(object_id):
    response = requests.get(f"{url}objects/{object_id}")
    return response


def create_an_object(dictionary):
    response = requests.post("https://api.restful-api.dev/objects", json=dictionary)
    return response
