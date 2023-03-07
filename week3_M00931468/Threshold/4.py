# Even or Odd
def evenOrOdd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

def main():
    while True:
        try:
            number = int(input('Enter a number: '))
            
        except:
            print('try again')
        else: 
            break
    evenOrOdd(number)

main()