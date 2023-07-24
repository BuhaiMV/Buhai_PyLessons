import datetime
# 1
import lesson_10

lesson_10.print_text_to_console('text')
print(lesson_10.add_ten_to_number(11))


# 2
def convert_text_number_to_int_number(text_number):
    try:
        return int(text_number)
    except ValueError as e:
        print(e)


convert_text_number_to_int_number('aaaa')


# 3
def change_the_date(date, days, symbol):
    if (symbol == True):
        return date + datetime.timedelta(days)
    elif (symbol == False):
        return date - datetime.timedelta(days)


print(change_the_date(datetime.datetime.now(), 15, True))


# 4
def your_age(date):
    age = int((datetime.datetime.now() - date).days / 365)
    age_timestamp = datetime.datetime.now().timestamp() - date.timestamp()
    return age, age_timestamp


print(your_age(datetime.datetime(2010, 10, 8, 14, 58, 14)))
