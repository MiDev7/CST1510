import random

num = random.randint(1,99)

print(num)
while True:
    value = int(input("Enter your number: "))
    if num == value:
        print("\tCongratulation, you got it!!!!")
        break
    while True:
        diff = num - value
        recentDiff = 0
        if recentDiff > diff:
            print("Your number is too large")
            break
        elif recentDiff < diff:
            print("Your number is too small")
            break
    
    