import re

# [abc] - [a-c]
# d - [0-9]
# D - [^0-9]
# s - [\n\t]
# S - [^\n\t]
# w - [a-zA-z0-9]
# W - [^a-zA-z0-9]
# * - >=0 matches
# + - >=1 matches
# ? - 0-1 matches
# {n} - n matches
# . - [^\n]
'''
pattern = re.compile('abc')
print(pattern)
res = pattern.match('dfabcdf')
print(res)
res = pattern.match('abcabcdf')
print(res)

pattern2 = re.compile('msg')
res = pattern2.search('msg1')
print(res)
res = pattern2.search('another msg1')
print(res)

pattern3 = re.compile('msg')
res = pattern3.findall('there`s a lot of msg, msg1, msg2, msg3')
print(res)
res = pattern3.finditer('there`s a lot of msg, msg1, msg2, msg3')
for i in res:
    print(i.span())
    print(i.group())
    print(i.start())
    print(i.end())

pattern = re.compile('\W')
result = pattern.split('there`s a lot of msg: msg1, msg2, msg3')
print(result)
result = pattern.split('there`s a lot of msg: msg1, msg2, msg3', 2)
print(result)
result = pattern.split('there`s a lot of msg: msg1, msg2, msg3', 3)
print(result)

result = re.split('\d', 'there`s a lot of msg: msg1, msg2, msg3')
print(result)

pattern = re.compile('blue|red|yellow')
result, number = pattern.subn('color', 'one yellow two red three green', count=2)
print(result)
print(number)
'''
pattern = 'a'
demo_str = "this is a string to count numbers of a symbols it. aa"
result = re.findall(pattern, demo_str)
print(result)
print(len(result))

pattern = 'test'
demo_str = 'this is a demo string to find test'
result = re.search(pattern, demo_str)
print(result)
result = re.search('test$', demo_str)  # $ - означає що закінчується цим
print(result)
result = re.search('^test', demo_str)  # ^ - означає що немає цього
print(result)
result = re.search('^test|test$', demo_str)  # | - означає або
print(result)
res = re.search('[0-9+]', 'string to find numbers 1 1')
print(res)
res = re.finditer('[0-9+]', 'string to find numbers 1 2')
for i in res:
    print(i.span())
    print(i.group())
res = re.findall('[0-9+]', 'string to find numbers 1 2')
print(res)
res = re.search('.*[0-9]?', '1 2')
print(res)
demo_str = 'https://site.com'
pattern = 'https://.*\.com'
result = re.search(pattern, demo_str)
print(result)
result = re.findall(pattern, 'fdgdfgdf https://sfsdfsdfsdfsdf.comasdasdasd https://site.comsdfsdfsdf')
print(result)
result = re.search(pattern, 'https://sfsd.fsdfsd.fsdf.comasdasdasd')
print(result)

demo_str = 'date1 = 12-05-2023 date2 = 13.05.2023 date2 = 13.05.2023'
pattern = '\d{2}[-./]\d{2}[-./]\d{4}'
result = re.findall(pattern, demo_str)
print(result)
demo_str = 'this?is.a.string?to?find/words^in@it'
result = re.findall('\w', demo_str)
print(result)
demo_str = 'mail@mail.com mail@mail.com'
result = re.findall('\w*@\w*\.com', demo_str)
print(result)
