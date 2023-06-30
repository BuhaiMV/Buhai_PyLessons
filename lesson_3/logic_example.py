import random

'''
first_value = input("print some number: ")
second_value = int(first_value)
if second_value > 5:
    print("text")
elif second_value < 3:
    print("third text")
else:
    print("second text")

first_value = input("print some number: ")
first_value = int(first_value)
if first_value * first_value > 100:
    print("number bigger 100")
else:
    print("number smallest 100")

first_value = 11
if first_value == int or first_value < 25:
    print("it`s above 20")

second_value = 16
if first_value <= 30 and first_value > 26:
    print('it`s above 13')

third_value = 5
if third_value > 4 and not third_value > 20:
    print('text 2')

print(bool(0))

eyes = int(input("number of eyes: "))
legs = int(input("number of legs: "))
if eyes == 8:
    if legs == 8:
        print("this is spider")
    elif legs == 6:
        print('this is fly')
    else:
        print("creature is undefined")
elif eyes == 1:
    print("this is odin")

answer = input("do you need more card? ")
if answer == 'yes':
    card = random.randint(1, 11)
    print(card)
    answer = input("do you need more card? ")
    if answer == 'yes':
        card += random.randint(1, 11)
        print(card)
        answer = input("do you need more card? ")
        if answer == 'yes':
            card += random.randint(1, 11)
            print(card)
            answer = input("do you need more card? ")
            if answer == 'yes':
                card += random.randint(1, 11)
                print(card)
                answer = input("do you need more card? ")
                if answer == 'yes':
                    card += random.randint(1, 11)
                    print(card)
                    answer = input("do you need more card? ")
                    if answer == 'yes':
                        card += random.randint(1, 11)
                        print(card)
                        answer = input("do you need more card? ")
                        if answer == 'yes':
                            card += random.randint(1, 11)
                            print(card)
print(f'you have: {card}')
card2 = random.randint(2, 21)
print(f'Ai have: {card2}')
if card > 21:
    print("you loose")
elif card > card2:
    print("you win")
else:
    print("you loose")

list_of_value = [2, 5, 3, 5, 8, 0, 'text', 9.0]
second_list_of_value = []
third_list_of_value = list()
print(len(list_of_value))
print(list_of_value[-1])
print(list_of_value.index(3))  # знайти за знченням
print(list_of_value)
list_of_value.append(8)  # додати в кінець
print(list_of_value)
list_of_value.insert(3, 11)  # додати на місце
print(list_of_value)
list_of_value.remove(5)  # видалити за значенням
print(list_of_value)
list_of_value.pop()  # видалити в кінці
print(list_of_value)
list_of_value.pop(0)  # видалити за індексом
print(list_of_value)
del list_of_value[1]  # видалити за індексом
print(list_of_value)
list_of_value.clear() # видалити весь ліст
print(list_of_value)
    '''
new_list = [9, 3, 6, 2, 6, 9, 5, 1]
second_new_list = [1, 2, 3, [1, 2, 3]]
new_list.sort()
print(new_list)
new_list.sort(reverse=True)
print(new_list)
print(new_list[:5])
print(new_list[1:])
second_new_list.extend(new_list)  # додав в кінець ліст
print(second_new_list)
