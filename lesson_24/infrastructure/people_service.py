from requests import get, Response
from lesson_24.app import config


class PeopleService:
    def __init__(self):
        self.__people_url = f'{config["host"]}/people/'

    def get_people(self, people_id) -> Response:
        return get(f"{self.__people_url}/{people_id}")

    
