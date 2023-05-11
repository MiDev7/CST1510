def passwordChecker():
    passwords = {'John':'12345', 'Anna':'Magic123','Sue':'Sue123'}
    username = str(input("Enter your username: "))


    count = 2
    while count != 0:
        for key in passwords.keys():
            if username == key:
                print("You enter a valid username")
                password = str(input("Enter your password: "))
                while count != 0:
                    if password == passwords[username]:
                        print("Welcome, you are successfully logged in")
                        count = 0
                    else: 
                        print(f"{count} attempt left.")
                        print("You entered an invalid password. please try again")
                        password = str(input("Enter your password: "))
                        count-=1
                        if count == 0:
                            print(f"You are out of attempts, please come back later")
                break
            else:
                continue
        if count != 0:
            print(f"{count} attempt left.")
            print("You entered a non-exisiting username, please try again")
            username = str(input("Enter your username: "))
            count-=1
            if count == 0:
                print(f"You are out of attempts, please come back later")       

passwordChecker()