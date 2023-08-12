from lesson_16.home_work.factory.dishes.dish import Dish


class Risotto(Dish):
    def __init__(self, size):
        super().__init__(size)
        self.name = 'Risotto'
        if self.size == 'small':
            self.price = 5
        elif self.size == 'medium':
            self.price = 7.5
        elif self.size == 'large':
            self.price = 10
        else:
            raise Exception('wrong size')

    def order(self):
        print(f'You order {self.name}, size: {self.size}, it`s cost: {self.price}$')
