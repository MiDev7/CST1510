import random

def lottery():
    generatedNumber=random.randint(10,99)

    print(generatedNumber)
    num = int(input('Enter your choice of numbers:\n'))

    if generatedNumber // 10 == num // 10 and generatedNumber % 10 == num % 10 :
        print('Congratulations, you won a total amount of £10000.')
    elif generatedNumber % 10 == num // 10 and generatedNumber // 10 == num % 10: 
        print('Congratulations, you won a total amount of £3000.')

    elif generatedNumber // 10 == num // 10 or generatedNumber % 10 == num % 10 or generatedNumber % 10 == num // 10 or generatedNumber // 10 == num % 10 :
        print('Congratulations, you won a total amount of £1000.')

def main():
    lottery()

main()