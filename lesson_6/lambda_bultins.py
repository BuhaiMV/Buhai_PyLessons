import math
import random
from functools import reduce


def func_name():
    pass


double = lambda x: x * 2

print(double(5))
print(double(3))


def to_cube(x):
    return x * x * x


lambda_3_to_cube = lambda: 3 * 3 * 3

print(to_cube(3))
print(lambda_3_to_cube())

sqrt_x = lambda x: math.sqrt(x)

print(sqrt_x(15))

lambda_list = [
    lambda x: x * 2,
    lambda x: x * 3,
    lambda x: x * 4
]
for el in lambda_list:
    print(el(1000))

lambda_tuple = (
    lambda x: x * 2,
    lambda x: x * 3,
    lambda x: x * 4
)
for el in lambda_tuple:
    print(el(1000))

lambda_dict = {
    'double': lambda x: x * 2,
    'triple': lambda x: x * 3,
    'quadruple': lambda x: x * 4
}

print(lambda_dict['double'](3))

areas_dict = {
    'circle': lambda r: math.pi * r * r,
    'rectangle': lambda a, b: a * b,
    'square': lambda a: a * a
}

print(f'площа фігури: {areas_dict["circle"](30)}')
print(f'площа фігури: {areas_dict["rectangle"](10, 20)}')
print(f'площа фігури: {areas_dict["square"](300)}')

# filter(func, list)
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x % 2 == 0, list_a))
print(filtered_list)
filtered_list = list(filter(lambda x: x % 2 != 0, list_a))
print(filtered_list)

# map(func, list)
double_list = list(map(lambda element: element * 2, list_a))
print(double_list)

# reduce(func, list)
summ_example = reduce(lambda value, element: value + element, list_a)
print(summ_example)

list_b = [90, 50, 20, 69]

min_el = reduce(lambda value, element: value if (value < element) else element, list_b)
print(min_el)
