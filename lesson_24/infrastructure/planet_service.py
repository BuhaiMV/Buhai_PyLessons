from requests import get, Response
from lesson_24.app import config


class PlanetService:
    def __init__(self):
        self.__planet_url = f'{config["host"]}/planets/'

    def get_planets(self, planet_id) -> Response:
        return get(f"{self.__planet_url}/{planet_id}")

    def go_to_page(self, number) -> Response:
        return get(f"{self.__planet_url}/?page={number}")

    def get_value(self, planet_id, name):
        response = self.get_planets(planet_id)
        return response.json()[name]
