def sumOfAllnum(num):
    total = 0
    for index in range(1, num + 1):
        if index % 3 == 0 :
            total = total + (index) 
        elif index % 5 == 0:
            print(index%5)
            total = total + (index) 
    print(f"The sum of all number until {num} is {total} ")

def main():
    inputNum = int(input("Enter the value of n: "))
    sumOfAllnum(inputNum)

main() % 5