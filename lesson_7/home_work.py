import re


# 1
def check_symbols(value):
    if (len(re.findall('\w|_', value)) == len(value)):
        return True
    else:
        return False


print(check_symbols('Aaa_456'))

# 2
list_for_delete = ["example (.com)", "github (.com)", "stackoverflow (.com)"]


def delete_inside_brackets(list_of_values):
    for index in range(len(list_of_values)):
        list_of_values[index - 1] = re.sub('\((.*?)\)', '', list_of_values[index - 1])


delete_inside_brackets(list_for_delete)
print(list_for_delete)
#3
def insert_space(string):
    string = re.sub('([A-Z])', r' \1', string)
    return string

print(insert_space('aAbZs'))
