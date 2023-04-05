def word_ascii(word):
    newword = ""
    for i in word:
        newword = newword + str(ord(i))
    return newword

def main():
    password = str(input("Enter a password: "))
    print(f"Your password in ASCII is: {word_ascii(password)}")

main()
