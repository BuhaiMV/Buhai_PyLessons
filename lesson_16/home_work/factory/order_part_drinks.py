from lesson_16.home_work.factory.drinks.cola import Cola
from lesson_16.home_work.factory.drinks.vine import Vine


class OrderPartDrinks:
    @staticmethod
    def get_order(name, size):
        if name == 'Cola':
            return Cola(size)
        elif name == 'Vine':
            return Vine(size)
        else:
            raise Exception('wrong dish')
