# first task
firstName = 'Maksym'
lastName = 'Buhai'
fullName = firstName + ' ' + lastName
# 1
print(firstName + ' ' + lastName)
# 2
print(fullName.lower())
print(fullName.upper())
print(fullName.title())
# 3
fullName = f'\t\n{fullName}\t'
print(fullName)
fullName = fullName.strip()
print(fullName)

# second task
dollar = 36.7
money = 1000 / dollar
money = round(money, 2)
print(f'Поточний курс складає: {money}')
