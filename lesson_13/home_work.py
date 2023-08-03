from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, wheels, color, fuel_type):
        self.wheels = wheels
        self.color = color
        self.fuel_type = fuel_type

        @abstractmethod
        def refuel(self):
            pass


class Electro(Car):
    def __init__(self, wheels, color, fuel_type):
        super().__init__(wheels, color, fuel_type)

    def refuel(self):
        pass


class Gasoline(Car):
    def __init__(self, wheels, color, fuel_type):
        super().__init__(wheels, color, fuel_type)

    def refuel(self):
        pass


class Tesla(Electro):
    def __init__(self, wheels, color, fuel_type):
        super().__init__(wheels, color, fuel_type)

    def refuel(self):
        print(f'car charged by {self.fuel_type}')


class Reno(Gasoline):
    def __init__(self, wheels, color, fuel_type):
        super().__init__(wheels, color, fuel_type)

    def refuel(self):
        print(f'car fueled by {self.fuel_type}')


model_s = Tesla(4, 'red', 'gasoline')
megan = Reno(4, 'green', 'electricity')
megan.refuel()
model_s.refuel()
