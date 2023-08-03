from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, salary, position):
        self.salary = salary
        self.position = position

    @abstractmethod
    def do_work(self):
        pass


class Toyota_employee(Employee):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('I`m doing Toyota stuff')


class Reno_employee(Employee):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('I`m doing Reno stuff')


employee = Toyota_employee('worker', 2000)

'''
class Car(ABC):
    def __init__(self, wheels, color, fuel_type):
        self.wheels = wheels
        self.color = color
        self.fuel_type = fuel_type

    @abstractmethod
    def go_straight(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

    @staticmethod
    def open_window():
        print('window is opened')


class Electro(Car):
    def __init__(self, wheels, color, fuel_type):
        super().__init__(wheels, color, fuel_type)

    def go_straight(self):
        print('car going straight')

    def refuel(self):
        print('car charged')


class Gasoline(Car):
    def __init__(self, wheels, color, fuel_type):
        super().__init__(wheels, color, fuel_type)

    def go_straight(self):
        print('car going straight')

    def refuel(self):
        print('car fueled')


gasoline_car = Gasoline(4, 'red', 'gasoline')
electro_car = Electro(4, 'green', 'electricity')
'''


class Engineer(Employee):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('I`m creating frameworks')

    def __create_new_framework(self):
        print('framework in progress')


class Programmer(Engineer):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('I`m writing programs')

    def _deploy_program(self):
        print('program is deploying')


engi = Engineer(2, '1')

