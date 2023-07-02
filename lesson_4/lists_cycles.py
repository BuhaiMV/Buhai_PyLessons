import random

'''
list_of_numbers = [5, 8, 3, 4, 8, 1, 3, 7, 4, 3]

list_of_numbers2 = []
for element in list_of_numbers:
    element = element + 5
    list_of_numbers2.append(element)
    # print(element)
# print(list_of_numbers2)
new_list_of_numbers = list_of_numbers.copy()
new_list_of_numbers2 = list_of_numbers
new_list_of_numbers3 = list(list_of_numbers)
new_list_of_numbers4 = list_of_numbers + new_list_of_numbers
# print(new_list_of_numbers)
for i in range(len(list_of_numbers)):
    list_of_numbers[i] += 5
print(list_of_numbers)
print(new_list_of_numbers)
print(new_list_of_numbers2)
print(new_list_of_numbers3)
print(new_list_of_numbers4)
print(new_list_of_numbers4.count(8))
new_list_of_numbers4.reverse()
print(new_list_of_numbers4)

list_of_numbers_reverse = []
for i in range(len(list_of_numbers)):
    list_of_numbers_reverse.append(list_of_numbers[len(list_of_numbers) - (i + 1)])

print(list_of_numbers_reverse)
new_tuple = (1, 2, 3)
for element in new_tuple:
    print(element)

while len(new_list_of_numbers) > 5:
    new_list_of_numbers.pop()
print(new_list_of_numbers)

counter = 0
while counter < 10:
    new_list_of_numbers.append(counter)
    counter += 1
print(new_list_of_numbers)

while counter < 100:
    a = random.randint(1, 10)
    print(a)
    if a == 10:
        break
    counter +=1

while counter < 10:
    a = random.randint(1, 10)
    # print(a)
    print(counter)
    if a == 10:
        continue
    counter += 1
value = 0
while True:
    value_temporary = input('print: ')
    if value_temporary == 'summ':
        break
    elif value_temporary.isnumeric():
        value += int(value_temporary)
        print(value)
    else:
        print('you input wrong word')
        continue
print(value)
'''
unique_value = {'A', 2, 2, 3, 4, 'B'}
print(unique_value)
list_with_doubles = ['a', 'a', 1, 1, 1, 1, 2, 2, 3, 3, 4]
new_set = set(list_with_doubles)
print(new_set)
list_without_doubles = list(new_set)
print(list_without_doubles)
print(16 not in unique_value)
second_unique_values = {2, 3, 4}
print(second_unique_values.issubset(unique_value))  # чи є перше всереденні другого
print(unique_value.issuperset(second_unique_values))  # чи немає першого всередені другого
third_uniq_value = {4, 5, 6}
print(third_uniq_value.union(second_unique_values))  # об'єднання
print(third_uniq_value.intersection(second_unique_values))  # що спільне
print(third_uniq_value.difference(second_unique_values))  # що різне
print(third_uniq_value.symmetric_difference(second_unique_values))  # об'єднати без спільного
# second_unique_values.update(third_uniq_value)
# second_unique_values.intersection_update(third_uniq_value)
# second_unique_values.difference_update(third_uniq_value)
second_unique_values.symmetric_difference_update(third_uniq_value)
print(second_unique_values)
second_unique_values.add(4)
print(second_unique_values)
second_unique_values.remove(6)
print(second_unique_values)
second_unique_values.discard(0)  # як remove тільки без помилки
print(second_unique_values)
second_unique_values.pop()
second_unique_values.pop()
print(second_unique_values)
second_unique_values.clear()
print(second_unique_values)
value = int()
value += 1
print(value)
