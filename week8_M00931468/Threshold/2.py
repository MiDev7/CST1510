def secret_word_compris(name, surname):
    special_word = name[:3] + surname[-2:]
    return special_word

def main():
    name= str(input("Enter your name: "))
    surname = str(input("Enter your surname: "))
    print(secret_word_compris(name,surname))

main()