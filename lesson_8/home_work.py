import re
import csv


# 1
def read_domains(file):
    with open(file, 'r') as domain:
        domain = domain.readlines()
        for index in range(len(domain)):
            domain[index - 1] = re.sub('\.|\\n', '', domain[index - 1])
        return domain


print(read_domains('files/domains.txt'))


# 2
def read_names(file):
    name = []
    with open(file, 'r') as file_with_names:
        file_with_names = csv.DictReader(file_with_names)
        for row in file_with_names:
            name.append(row['name'])
    return name


print(read_names('files/names.txt'))


# 3
def read_dates(file):
    dates = []
    with open(file, 'r') as file_with_dates:
        file_with_dates = file_with_dates.readlines()
        for line in file_with_dates:
            days = '[\w]+'
            month = '[a-zA-Z]+'
            years = '[0-9]+'
            result = re.findall(f'{days}[" "]{month}[" "]{years}|{month}[" "]{years}', line)
            if len(result) > 0:
                dates.append({'date': result[0]})
    return dates



print(read_dates('files/authors.txt'))
