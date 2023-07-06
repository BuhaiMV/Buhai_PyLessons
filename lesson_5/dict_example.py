field = 'field'
cat = {'name': 'Tom', 'age': 5, 'goodboy': True, 'locations': ['home', ['yard', field]]}
print(cat['name'])
print(cat)
print(len(cat))
del (cat['locations'])
print(cat)
print('name' not in cat)
cat2 = cat.copy()
print(id(cat))
print(id(cat2))
print(cat.get('age'))
print(cat.items())
print(cat.keys())
print(cat.values())
# print(cat.pop('goodboy'))
print(cat)

print(cat.popitem())
print(cat)
cat.update({'fur': 'black', 'eye_color': 'green'})
cat['tail'] = True
print(cat)
cat.update({'fur': 'red'})
cat['name'] = 'Jerry'
print(cat)
cat.update(cat2)
print(cat)

'''
first_value = 5
second_value = first_value
print(id(first_value))
print(id(second_value))
second_value = 7
print(id(first_value))
print(id(second_value))
'''
first_list = [1, 2, 3]
second_list = first_list
print(first_list)
print(second_list)
print(id(first_list))
print(id(second_list))
second_list[0] = 12
print(id(first_list))
print(id(second_list))
print(first_list)
print(second_list)
'''
не змінюванні - string, int, cort, float, bool
змінюванні - list, dict, set
'''
print(first_list == second_list)
print(first_list is second_list)  # перевіряє id
third_list = first_list.copy()
fourth_list = list(first_list)
print(first_list == third_list)
print(third_list is first_list)
print(first_list == fourth_list)
print(fourth_list is first_list)
