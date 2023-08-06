import datetime
from abc import ABC, abstractmethod


class MuseumStaff(ABC):
    def __init__(self, name: str, year: int, place: str, fans: int, material=None):
        self.__name = name
        self.material = material
        self.year = year
        self.place = place
        self.fans = fans

    @property
    def name(self):
        return self.__name

    def change_fans_amount(self, new_amount):
        self.fans = new_amount

    @staticmethod
    def welcome():
        print('Welcome to museum')

    @abstractmethod
    def about(self):
        pass


class Picture(MuseumStaff):
    def __init__(self, name: str, year: int, place: str, fans: int):
        super().__init__(name, year, place, fans)
        self.material = 'Paper'

    def __about_name(self):
        print(f'This is {self.name}')

    def __about_year(self):
        print(f'they {datetime.datetime.now().year - self.year} years old')

    def __about_place(self):
        print(f'they stay at {self.place}')

    def about(self):
        self.__about_name()
        self.__about_year()
        self.__about_place()
        print('have a good time!')


class Statue(MuseumStaff):
    def __init__(self, name: str, material, year: int, place: str, fans: int):
        super().__init__(name, year, place, fans)
        self.material = material

    def __about_name(self):
        print(f'This is {self.name}')

    def __about_material(self):
        print(f'made of {self.material}')

    def __about_year(self):
        print(f'they {datetime.datetime.now().year - self.year} years old')

    def __about_place(self):
        print(f'they stay at {self.place}')

    def about(self):
        self.__about_name()
        self.__about_material()
        self.__about_year()
        self.__about_place()
        print('have a good time!')


mona_lisa = Picture('Mona Lisa', 1503, '3rd room in north section', 100500)
mona_lisa.welcome()
mona_lisa.about()
venus_de_milo = Statue('Venus de Milo', 'marble', 150, '1st room in west section', 100500)
venus_de_milo.welcome()
venus_de_milo.about()
