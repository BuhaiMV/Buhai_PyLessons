from lesson_16.home_work.factory.order_part_dishes import OrderPartDishes
from lesson_16.home_work.factory.order_part_drinks import OrderPartDrinks
import datetime


class Order:
    def __init__(self):
        self.orders = []

    def get_order(self, type_of_order, name, size):
        time = datetime.datetime.now()
        self.orders.append({'name': name,
                            'time': {'year': time.year, 'month': time.month, 'day': time.day, 'hour': time.hour,
                                     'minute': time.minute, 'second': time.second}})
        if type_of_order == 'Dish':
            return OrderPartDishes().get_order(name, size)
        elif type_of_order == 'Drink':
            return OrderPartDrinks().get_order(name, size)
        else:
            raise Exception('wrong type')


orders_factory = Order()
order1 = orders_factory.get_order('Drink', 'Cola', 'small')
order1.order()
order2 = orders_factory.get_order('Dish', 'Pizza', 'large')
print(orders_factory.orders)
