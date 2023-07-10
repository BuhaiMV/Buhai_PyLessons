def function_for_find_number_in_rang(number, max_rang, min_rang=0):
    if number > min_rang and number < max_rang:
        return True
    else:
        return False


print(function_for_find_number_in_rang(1, 6, 2))


def del_symbols_from_string(list_of_symbols, string):
    for element in list_of_symbols:
        string = string.replace(element, '')
    return string


print(del_symbols_from_string(['ta', 'b'], 'attakbo'))
