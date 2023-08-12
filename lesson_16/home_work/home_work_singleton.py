# 1
def singleton(_class):
    def inner(*args):
        if not hasattr(_class, 'instance'):
            setattr(_class, 'instance', _class(*args))
        return getattr(_class, 'instance')

    return inner


@singleton
class Car:
    def __init__(self, model, color, doors):
        self.model = model
        self.color = color
        self.doors = doors


tesla1 = Car('model s', 'red', 2)
tesla2 = Car('model y', 'green', 4)
print(tesla1.model)
print(tesla2.model)
