import requests

url = "https://api.restful-api.dev/"


def get_an_object(object_id):
    response = requests.get(f"{url}objects/{object_id}")
    return response.json(), response.status_code


def create_an_object(dictionary):
    response = requests.post("https://api.restful-api.dev/objects", json=dictionary)
    return response.json(), response.status_code


def update_an_object(object_id, dictionary):
    response = requests.put(f"https://api.restful-api.dev/objects/{object_id}", json=dictionary)
    return response.json(), response.status_code


def delete_an_object(object_id):
    response = requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    return response.json(), response.status_code
