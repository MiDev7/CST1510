def main():
    while True:
        try:
            x, y = input("Enter two integers value: ").split()
            x = int(x)
            y = int(y) 
            answer = x * y
            if answer == (x * y):
                print(f"The product of {x} x {y} = {answer}")
                break
        except:
            print("Please try again input only integer value")




main()