# Dog Years
def dogYears():
    while True:
        humanDogAge =  int(input('Enter your dog\'s age: '))
        if humanDogAge < 0:
            print('Enter a valid dog age')
        else:
            break

    if humanDogAge <= 2:
        dogAge = humanDogAge * 10.5
        print(f'Your dog have {dogAge} dog years')

    else:
        humanDogAge -= 2
        dogAge = 21 + (humanDogAge * 4)
        print(f'Your dog have {dogAge} dog years.')

def main():
    dogYears()

main()

