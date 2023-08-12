from lesson_16.home_work.factory.dishes.risotto import Risotto
from lesson_16.home_work.factory.dishes.pasta import Pasta
from lesson_16.home_work.factory.dishes.pizza import Pizza


class OrderPartDishes:
    @staticmethod
    def get_order(name, size):
        if name == 'Risotto':
            return Risotto(size)
        elif name == 'Pasta':
            return Pasta(size)
        elif name == 'Pizza':
            return Pizza(size)
        else:
            raise Exception('wrong dish')
