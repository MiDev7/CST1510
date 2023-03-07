# Vowel or Consonants
def vowelOrConsonants():
    character = str(input('Enter a character:')).lower()
    
    if character == 'a' or character == 'e' or  character == 'i' or  character == 'o' or  character == 'u':
        print(f'{character} is a vowel')

    elif character == 'y':
        print(f'{character} is sometimes a vowel, and sometimes {character} is consonant')  
    
    else:
        print(f'{character} is a consonant')

def main():
    vowelOrConsonants()

main()