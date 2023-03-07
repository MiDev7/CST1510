import random

def lottery():
    generatedNumber=random.randint(100,999)

    print(generatedNumber)
    num = int(input('Enter your choice of numbers:\n'))

    generated100 = generatedNumber % 100
    remainder100 = num % 100

    firstRandInt = generatedNumber // 100
    secondRandInt = generated100 // 10
    thirdRandInt = generated100 % 10

    firstInt = num // 100
    secondInt = remainder100 // 10
    thirdInt = remainder100 % 10

    if firstRandInt == firstInt and secondRandInt == secondInt and thirdRandInt == thirdInt :
        print('Congratulations, you won a total amount of £10000.')
    elif (firstRandInt == secondInt and secondRandInt == firstInt and thirdRandInt == thirdInt) or (firstRandInt == secondInt and secondRandInt == firstInt and thirdRandInt == thirdInt) or (firstRandInt == firstInt and secondRandInt == thirdInt and thirdRandInt == secondInt) or (firstRandInt == thirdInt and secondRandInt == firstInt and thirdRandInt == secondInt) or (firstRandInt == thirdInt and secondRandInt == secondInt and thirdRandInt == firstInt) : 
        print('Congratulations, you won a total amount of £3000.')

    elif (firstRandInt == firstInt or firstRandInt == secondInt or firstRandInt == thirdInt) or (secondRandInt == firstInt or secondRandInt == secondInt or secondRandInt == thirdInt) or (thirdRandInt == firstInt or thirdRandInt == secondInt or thirdRandInt == thirdInt): 
        print('Congratulations, you won a total amount of £1000.')

def main():
    lottery()

main()