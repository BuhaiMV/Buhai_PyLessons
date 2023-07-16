import csv

with open('files/birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)

with open('files/birthday.txt', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)
'''
with open('birthday.csv', 'w') as birthday:
    birthday_writer = csv.writer(birthday, delimiter=',', quotechar=";")
    birthday_writer.writerow(['Markus', 'python', 2])
    birthday_writer.writerow(['Alejandro', 'c++', 4])
'''
with open('files/birthday.csv', 'w') as birthday:
    birthday_fieldnames = ['name', 'group', 'birthday']
    birthday_dict_writer = csv.DictWriter(birthday, fieldnames=birthday_fieldnames)
    birthday_dict_writer.writeheader()
    birthday_dict_writer.writerow({'name': 'Markus', 'group': 'python', 'birthday': '2'})
    birthday_dict_writer.writerow({'name': 'Alejandro', 'group': 'c++', 'birthday': '4'})
    birthday_dict_writer.writerows([{'name': 'Markus', 'group': 'python', 'birthday': '2'}, {'name': 'Alejandro', 'group': 'c++', 'birthday': '4'}])
