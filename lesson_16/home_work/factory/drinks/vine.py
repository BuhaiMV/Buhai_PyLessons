from lesson_16.home_work.factory.drinks.drink import Drink


class Vine(Drink):
    def __init__(self, size):
        super().__init__(size)
        self.name = 'Vine'
        if self.size == 'small':
            self.price = 3
        elif self.size == 'medium':
            self.price = 4.5
        elif self.size == 'large':
            self.price = 6
        else:
            raise Exception('wrong size')

    def order(self):
        print(f'You order {self.name}, size: {self.size}, it`s cost: {self.price}$')
