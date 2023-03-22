import random

totalQuestion = 0
point = 0

def addition():
    global totalQuestion 
    global point
    while True:
        number1 = random.randint(0,9)
        number2 = random.randint(0,9)
        totalQuestion += 1
        while True:
            userAns = int(input(f"{number1} + {number2} = "))
            answer = number1 + number2
            if userAns == answer:
                point += 1
                print("You are correct")
                break
            else:
                print("You are wrong!!")
                break
        print(f"You total score is {point}/{totalQuestion}.")

        choice = str(input("Would you like to continue practicing Addition(Y/N): ")).lower()
        if choice != "y":
            break    
        
def multiplication():
    global totalQuestion 
    global point
    while True:
        number1 = random.randint(0,9)
        number2 = random.randint(0,9)
        totalQuestion += 1
        while True:
            userAns = int(input(f"{number1} x {number2} = "))
            answer = number1 * number2
            if userAns == answer:
                point += 1
                print("You are correct")
                break
            else:
                print("You are wrong!!")
                break
        print(f"You total score is {point}/{totalQuestion}.")                
        choice = str(input("Would you like to continue practicing Multiplication(Y/N): ")).lower()
        if choice != "y":
            break
        
def substraction():
    global totalQuestion 
    global point
    while True:
        number1 = random.randint(0,9)
        number2 = random.randint(0,9)
        totalQuestion += 1
        while True:
            userAns = int(input(f"{number1} - {number2} = "))
            answer = number1 - number2
            if userAns == answer:
                point += 1
                print("You are correct")
                break
            else:
                print("You are wrong!!")
                break
        print(f"You total score is {point}/{totalQuestion}.")                    
        choice = str(input("Would you like to continue practicing Substraction(Y/N): ")).lower()
        if choice != "y":
            break
        
def division():
    global totalQuestion 
    global point
    while True:
        number1 = random.randint(0,9)
        number2 = random.randint(0,9)
        totalQuestion += 1
        while True:
            userAns = eval(input(f"{number1} / {number2} = "))
            try:
                answer = number1/number2
            except ZeroDivisionError:
                answer = 0
            if userAns == round(answer,2):
                point += 1
                print("You are correct")
                break
            else:
                print("You are wrong!!")
                break
        print(f"You total score is {point}/{totalQuestion}.")
        choice = str(input("Would you like to continue practicing Division(Y/N): ")).lower()
        if choice != "y":
            break
        
def remainder():
    global totalQuestion 
    global point
    while True: 
        number1 = random.randint(0,9)
        number2 = random.randint(0,9)
        totalQuestion += 1
        while True:
            userAns = eval(input(f"what is the remainder of {number1} / {number2}? \n "))
            try:
                answer = number1%number2
            except ZeroDivisionError:
                answer = 0
            if userAns == answer:
                point += 1
                print("You are correct")
                break
            else:
                print("You are wrong!!")
                break
        print(f"You total score is {point}/{totalQuestion}.")
        choice = str(input("Would you like to continue practicing Remainder(Y/N): ")).lower()
        if choice != "y":
            break
        
def power():
    global totalQuestion 
    global point
    while True:
        number1 = random.randint(0,9)
        number2 = random.randint(0,9)
        totalQuestion += 1
        while True:
            userAns = int(input(f"{number1} ** {number2} = "))
            answer = number1 ** number2
            if userAns == answer:
                point += 1
                print("You are correct")
                break
            else:
                print("You are wrong!!")
                break
        print(f"You total score is {point}/{totalQuestion}.")
        choice = str(input("Would you like to continue practicing Power(Y/N): ")).lower()
        if choice != "y":
            break  


def main():
    while True:
        topic = int(input("""
Welcome user to the First Grader Math Practice Programme(FGMPR):

Here is the practice topics list:
    1.  Addition
    2.  Multiplication
    3.  Substraction
    4.  Division
    5.  Remainder
    6.  Exponent

Enter you topic number:

"""))
        
         
        
        match topic:    
            case 1:           
                
                addition()

            case 2:
                
                multiplication()

            case 3:
                
                substraction()

            case 4:
                
                division()

            case 5:
                
                remainder()
                
            case 6:
                
                power()
        finalChoice = str(input("Would you like to continue practicing (Y/N): ")).lower()
        if finalChoice != "y":
            break                     
            


main()