def count_characters(password):
    lower = 0
    upper = 0
    digits = 0
    special = 0

    # Counting every character within the password
    for i in password:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
        elif i.isdigit():
            digits+=1
        else:
            special+=1


    print(
    f"""Counting character in your password: {password}
    Number of lower case charater: {lower}
    Number of upper case charater: {upper}
    Number of digits: {digits}
    Number of special character: {special}
    """)

def main():
    passwords = ["P@ssw0rd!","Pyth0nRul3s!","Sn@k3yCod3!","2PyTh0n2Furi0us!","c0d3r$p0w3r!","3y3s0fPyTh0n!","M0ntYpYth0n!","B1t3ThePyth0n!","Pyth0nF@ng!","Pr0gramm1ngG3nius!"]

    count_characters("P@#yn26at^&i5ve")
    for password in passwords:
        count_characters(password)

main()