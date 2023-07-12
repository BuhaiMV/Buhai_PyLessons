# 1
list_one = [1, 2, 3, 4]
list_two = [3, 4, 5, 6]
list_of_intersection = lambda first_list, second_list: list(set(first_list).intersection(second_list))
print(list_of_intersection(list_one, list_two))

# 2
is_number_checker = lambda value: value.isnumeric() if type(value) == str else "not a string"
print(is_number_checker('5'))

# 3
list_three = [7, 8, 9, 10, 11]
list_four = [7, 8, 9]
max_min_list_finder = lambda *lists: print(f'max list: {max(lists, key=len)}\nmin list: {min(lists, key=len)}')
max_min_list_finder(list_one, list_two, list_three, list_four)
