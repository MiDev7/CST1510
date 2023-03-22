# Sum of the First n Positive Integers 
while True:
    n = int(input("Enter a value for n: \n"))
    if n <= 0:
        print('Re-enter another positive value again')
    else:
        break


sumOfn = ((n)*(n+1))/2 

print(f'The sum of the first {n} is {int(sumOfn)} .')