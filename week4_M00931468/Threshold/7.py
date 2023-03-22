import random

number1 = random.randint(0,9)
number2 = random.randint(0,9)

def question(num1, num2):
    while True:
        answer = int(input(f'What is {num1} x {num2}:\n '))

        if answer == (num1 * num2):
            print('You are correct')
            break
        else:
            print('Oops, try again!')
        
    
def main():
    question(number1,number2)
    

main()