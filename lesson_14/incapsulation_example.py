from abc import ABC, abstractmethod


class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name


class Cat:
    def make_noise(self):
        pass


class Lion(Cat):
    def __init__(self):
        self.color = 'yellow'
        self.age = 12
        self.speed = 60
        self.character = 'Pride'

    def make_noise(self):
        print('Roar')


class Cheetah(Cat):
    def __init__(self):
        self.color = 'Black'
        self.age = 10
        self.speed = 120
        self.character = 'Friendly'

    def make_noise(self):
        print('Meow')


king = Lion()
sweet_cheetah = Cheetah()
king.make_noise()
sweet_cheetah.make_noise()


class Road(ABC):
    def __init__(self, name: str, cover: str, length: int, bridge: int, crossroads: int):
        self.__name = name
        self.cover = cover
        self.length = length
        self.bridge = bridge
        self.crossroads = crossroads

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @abstractmethod
    def add_bridge(self):
        pass

    @staticmethod
    def length_between_bridges(length, bridges):
        return length / bridges


class Highway(Road):
    def __init__(self, name: str, cover: str, length: int, bridge: int, crossroads: int):
        super().__init__(name, cover, length, bridge, crossroads)
        self.cover = 1

    def __prepare_for_bridge(self):
        print('All preparations are ready')

    def __prepare_place(self):
        print('place are ready')

    def __prepare_docs(self):
        print('All docs are ready')

    def __finish(self):
        self.bridge += 1

    def add_bridge(self):
        self.__prepare_for_bridge()
        self.__prepare_place()
        self.__prepare_docs()
        self.__finish()
        print(f'Bridge is ready, we have {self.bridge} bridges')


class DirtyRoad(Road):
    def __init__(self, name: str, cover: str, length: int, bridge: int, crossroads: int):
        super().__init__(name, cover, length, bridge, crossroads)

    def __prepare_for_bridge(self):
        print('All preparations are ready')

    def __prepare_docs(self):
        print('All docs are ready')

    def __finish(self):
        self.bridge += 1

    def add_bridge(self):
        self.__prepare_for_bridge()
        self.__prepare_docs()
        self.__finish()
        print(f'Bridge is ready, we have {self.bridge} bridges')


road66 = Highway('road 66', 1, 3000, 4, 7)
road78 = DirtyRoad('road 78', 0, 768, 2, 7)
road66.add_bridge()
road78.add_bridge()
print(road66.length_between_bridges(3000, 4))
road66.name = 'Road 66'
print(road66.name)
