from lesson_16.home_work.factory.dishes.dish import Dish


class Pizza(Dish):
    def __init__(self, size):
        super().__init__(size)
        self.name = 'Pizza'
        if self.size == 'small':
            self.price = 4
        elif self.size == 'medium':
            self.price = 6
        elif self.size == 'large':
            self.price = 8
        else:
            raise Exception('wrong size')

    def order(self):
        print(f'You order {self.name}, size: {self.size}, it`s cost: {self.price}$')
