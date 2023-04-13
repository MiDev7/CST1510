def validatePassword(password):
    if password.isspace():
        print("Your password contains a space remove the space")
        return False
    if password.isupper() and password.islower() and password.isdigit() and not(password.isalpha() or  password.isdigit() or not password.isspace()):
        return True
        

if __name__ == "__main__":
    password = str(input("Enter a password: "))
    print(validatePassword(password))