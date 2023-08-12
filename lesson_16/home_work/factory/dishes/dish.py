from abc import ABC, abstractmethod


class Dish(ABC):
    def __init__(self, size):
        self.size = size
    @abstractmethod
    def order(self):
        pass
