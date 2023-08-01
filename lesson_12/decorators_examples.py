import datetime


def percent(func):
    def inner(msg):
        header, footer = "%" * 20, "%" * 20
        return f"{header}\n{func(msg)}\n{footer}"

    return inner


def and_symbol(func):
    def inner(msg):
        header, footer = "&" * 20, "&" * 20
        return f"{header}\n{func(msg)}\n{footer}"

    return inner


def add_footer_header(sign, quantity):
    def middle_level(func):
        def inner(some_msg):
            footer = sign * quantity
            header = sign * quantity
            return f'{header}\n{func(some_msg)}\n{footer}'

        return inner

    return middle_level


# @and_symbol
# @percent
@add_footer_header('#', 10)
def hi(msg):
    return "***\n" + msg + "\n***"


print(hi('hello my fellow friends'))


def timer_function(func):
    def timer(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        print(datetime.datetime.now() - start)
        return result

    return timer


@timer_function
def mega_math(first_value, second_value):
    for i in range(100000):
        first_value * second_value
    return 'done'


print(mega_math(5, 10))
