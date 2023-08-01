'''class Human:
    name = 'Andy'
    age = 30
    address = []


andy: Human = Human()
samantha: Human = Human()
print(Human)
print(andy)
samantha.name = 'Samantha'
print(samantha.name)
print(andy.name)
samantha.address = ['1 avenue']
andy.address = ['2 avenue']
andy.address.append('5')
print(andy.address)
print(samantha.address)'''


class Human:
    def __init__(self, name, age, address, hair_color):
        self.__name = name  # спрятав але можно достучатися
        self.__age = age  # спрятав та не достучатися
        self.address = address
        self.hair_color = hair_color

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def modify_age(self, new_age):
        self.__age = new_age

    @classmethod
    def from_age_and_name(cls, name, age):
        return cls(name, age, '2 avenue', 'green')

    @staticmethod
    def get_me_something():
        print('hello')


francenshtein = Human.from_age_and_name('Francenshtein', 50)
andy = Human('Andy', 30, '1 avenue', 'black')
samantha = Human('Samantha', 25, None, None)
print(francenshtein.hair_color)
samantha.get_me_something()
samantha.modify_age(26)
samantha.name = 'Samantha 2000 pro'
print(samantha.name)
