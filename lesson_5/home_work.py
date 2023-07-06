import random

# 1
first_list = [1, 5, 2, 3, 4]
second_list = [5, 3, 4, 5, 6]


def find_same_numbers_and_print(list1, list2):
    list_of_uniq_values = list(set(list1).intersection(set(list2)))
    list_of_uniq_values.sort()
    for element in list_of_uniq_values:
        print(element)


find_same_numbers_and_print(first_list, second_list)

# 2
dict_of_students = {'Alex': 50, 'John': 70, 'Tom': 100, 'Sam': 40}


def find_middle_rating_of_dict_and_print(dict):
    all_marks = 0
    for element in dict.values():
        all_marks += element
    middle_rating = all_marks / len(dict)
    for element in dict:
        if dict[element] > middle_rating:
            print(element)


find_middle_rating_of_dict_and_print(dict_of_students)

# 3
name = ['Alex', 'John', 'Tom', 'Sam']
surname = ['Smith', 'Johnson', 'Williams', 'Brown']
location = ['USA', 'Great Britain', 'Australia', 'Canada']


def dict_creator(names, surnames, locations):
    new_dict = {'name': names[random.randint(0, len(names) - 1)],
                'surname': surnames[random.randint(0, len(surnames) - 1)],
                'location': locations[random.randint(0, len(locations) - 1)]}
    return new_dict


print(dict_creator(name, surname, location))
