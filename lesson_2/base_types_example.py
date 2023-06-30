import math
import random

'''
firs_value = 2  # int
g_value = 9.8  # float
message = 'This is message'  # float
result = True  # bool
empty_result = None  # NoneType
print(firs_value)
print(type(firs_value))
print(id(firs_value))

second_value = 4


print(math.pi * 2 ** 2)
print(random.choice(['first', 'second']))
'''

print(dir('aaaaa'))

my_name = 'my name'
# print(my_name.title())
# print(my_name.upper())
# print(my_name)
first_name = 'batman'
second_name = 'joker '
full_name = first_name + ' ' + second_name
print(full_name.strip())
print(full_name.capitalize())
print(full_name.title())
print(full_name.replace('joker', 'hardly'))
print('batman' in full_name)
print(first_name.isalpha())
print(full_name.count('a'))
print(full_name.index('a'))
print(full_name.find('a'))
print(len(full_name))
print(full_name.split())
print('first\nsecond'.splitlines())
print(full_name[3])
print(full_name[3:])
print(full_name[:4])
print(full_name[3:10])
print(full_name[3:6:2])
food = 'solvanka'
price = 90
print(f'Food is {food} and price is {price}')
input_value = input()
int_value = int()
print(input_value)
