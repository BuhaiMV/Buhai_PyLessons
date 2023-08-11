'''import datetime


class TrafficLight:
    numbers_someone_called_height = []

    def __init__(self):
        self.__color = 'green'
        self.height = 3

    def __str__(self):
        return f'Hi I`m traffic_light instance, and my current color_status is {self.__color}'

    def __repr__(self):
        return 'TrafficLight()'

    def __getattr__(self, item):
        return f'this is not {item} you are looking for'

    def __getattribute__(self, item):
        if item.startswitch('height'):
            TrafficLight.numbers_someone_called_height.append(datetime.datetime.now())
        return super().__getattribute__(item)


traffic_light_1 = TrafficLight()
print(traffic_light_1)
#traffic_light_2 = eval(repr(traffic_light_1))
#print(traffic_light_2)
print(traffic_light_1.height)
print('a')'''


class Horse:
    def __init__(self):
        self.speed = 5
        self.age = 4

    def __add__(self, other):
        return Mul(other.strength, self.speed)

    def __iadd__(self, other):
        self.age += other.age

    def __eq__(self, other):
        return self.age == other.age


class Donkey:
    def __init__(self):
        self.strength = 10
        self.age = 5

    def __add__(self, other):
        return Mul(other.speed, self.strength)


class Mul:
    def __init__(self, strength, speed):
        self.strength = strength
        self.speed = speed

    def __str__(self):
        return f'{self.__class__.__name__}\nspeed: {self.speed}\nstrength: {self.strength}'


horse = Horse()
horse2 = Horse()
donkey = Donkey()
mul = horse + donkey
mul2 = donkey + horse
print(mul)
print(mul2)
horse2 += donkey
print(horse2)
print(horse2 == horse)
