def function_example(param1, param2='Alex'):
    print(f'hello {param1}')
    print(f'and meet the {param2}')


name = 'Tom'
function_example('first', name)  # позиційні аргументи
function_example(param1='second', param2=name)  # іменовані аргументи
function_example(param2='second and first', param1=name)
function_example('third')


def summ_of_numbers(first, second):
    result = first + second
    return result


new_value = summ_of_numbers(5, 10)
new_value2 = summ_of_numbers(10, 20)
new_value3 = summ_of_numbers(new_value, new_value2)
print(new_value3)


def summ_and_multiply(first, second):
    result_of_summ = summ_of_numbers(first, second)
    result_of_multiply = first * second
    return result_of_summ, result_of_multiply


first_result, second_result = summ_and_multiply(5, 20)
print(first_result)
print(second_result)


def multiple_param(*param):  # *args довільна кільскість агументів
    for element in param:
        print(element)


multiple_param(1, 2, 3, 'a', 'b')


def multiple_named_param(**user_info):  # **kwargs довільна кількість іменованих аргументів
    for key, value in user_info.items():
        print(f'{key}: {value}')


multiple_named_param(first_name='Alex', second_name='Tom')
