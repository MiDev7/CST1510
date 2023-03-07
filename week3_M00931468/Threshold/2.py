import random

number =random.randint(0,100)

if number % 5 == 0:
    print('HiFive')

if number % 2 == 0:
    print('HiEven')

if number != 2 and number != 5 :
    print('HiNumber')

