'''
some_list = [1, 2, 3, 4, 5]
new_list = []
for item in some_list:
    if item > 3:
        new_list.append(item)

print(new_list)

new_list_comprehensions = [item ** 2 for item in some_list if item > 3]
print(new_list_comprehensions)

new_list = [item ** 2 for item in range(1000)]
print(new_list)

names = ['James', 'Jennifer', 'Jack']
new_dict = {index: name for index, name in enumerate(names)}
print(new_dict)


new_set = {item for item in [1, 1, 2, 2, 4, 6, 7, 8, 16, 8, 10]}
print(new_set)
'''
new_gen = (item for item in range(10000))
print(new_gen)
new_tuple = (*(item for item in range(10000)),)
print(new_tuple)
