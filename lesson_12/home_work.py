import random


# 1
class Dog:
    def __init__(self, name, fur_color, tail=False):
        self.name = name
        self.fur_color = fur_color
        self.tail = tail

    @staticmethod
    def bark():
        print("AUF")

    def dog_name(self):
        print(f'Dog name is {self.name}')

    def tail_length(self):
        if not self.tail:
            print("Dog didn't have a tail")
        else:
            print(f'Length of tail {self.tail}')

    def fur(self):
        print(f'Fur color {self.fur_color}')


doggy = Dog('Sirko', 'red')
doggy.bark()
doggy.tail_length()
doggy.fur()


# 2
class Company:
    def __init__(self, name, capital, logo: bool, ceo=False):
        self.name = name
        self.logo = logo
        self.capital = capital
        self.ceo = ceo

    @classmethod
    def small_company(cls, name, capital, ceo):
        return cls(name, capital, False, ceo)

    def ceo_name(self):
        if not self.ceo:
            print("Company didn't have a CEO")
        else:
            print(f'CEO of the company is {self.ceo}')

    def company_name(self):
        print(f'Company name is {self.name}')

    def capital_amount(self):
        print(f'Company have {self.capital}')

    def has_logo(self):
        if self.logo:
            print('Company have logo')
        else:
            print("Company didn't have logo")


twitter = Company.small_company('twitter', '100500$', 'Mask')
twitter.company_name()
twitter.capital_amount()
twitter.has_logo()


# 3
def function_name_writer(func):
    def writer(*args, **kwargs):
        print(f'function name: {func.__name__}')
        result = func(*args, **kwargs)
        return result

    return writer


@function_name_writer
def mega_add(value1, value2):
    print(value1 + value2)


@function_name_writer
def mega_multiplication(value1, value2):
    print(value1 * value2)


mega_add(5, 2)
mega_multiplication(4, 6)

new_list = [random.randint(1, 10) for i in range(100)]


# 4
def counter(list_of_numbers):
    for i in range(11):
        if i == 0:
            continue
        counters = 0
        for item in list_of_numbers:
            if i == item:
                counters += 1
        print(f'in list we have {counters} of {i}')


counter(new_list)
