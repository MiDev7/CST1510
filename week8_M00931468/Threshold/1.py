def main():
    while True:
        password = str(input("Enter your password: "))
        if (len(password) > 8):
            print("Valid password")
            break
        else:
            print("Invalid Password, try again ....")
            continue

main()