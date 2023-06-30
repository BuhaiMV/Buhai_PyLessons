import random

# 1
minute = random.randint(0, 59)
if minute >= 14 and minute <= 29:
    print('second')
elif minute >= 30 and minute <= 44:
    print('third')
elif minute >= 45:
    print('fourth')
else:
    print('first')

# 2
birth_month = int(input("number of your birth moth: "))
if birth_month == 1 or birth_month == 2 or birth_month == 12:
    print('За вікном падав сніг.')
elif birth_month >= 3 and birth_month <= 5:
    print('Все довкола розцвітало.')
elif birth_month >= 6 and birth_month <= 8:
    print('Діти насолоджувались літніми канікулами.')
elif birth_month >= 9 and birth_month <= 11:
    print('Все довкола загоралось яскравими фарбами.')
else:
    print('wrong month')

# 3
x = int(input("x: "))
y = int(input("y: "))
if x > 0 and y > 0:
    print('first')
elif x > 0 and y < 0:
    print('second')
elif x < 0 and y < 0:
    print('third')
elif x < 0 and y > 0:
    print('fourth')
elif x == 0 and y != 0:
    print('on X line')
elif x != 0 and y == 0:
    print('on Y line')
else:
    print('on middle spot')
