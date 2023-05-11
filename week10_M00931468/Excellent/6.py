morseDict = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'J':'.---',
    'I':'..',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
    '?':'..--..',
    '!':'-.-.--',
    '.':'.-.-.-',
    ',':'--..--',
    ';':'-.-.-.',
    ':':'---...',
    '+':'.-.-.',
    '-':'-....-',
    '/':'-..-.',
    '=':'-...-'}

def morseEncoder(text):
    morseChar = ''
    morse = []
    temp = []
    for char in text:
        if char == ' ':
            temp.append('/ ')
            continue
        morseChar = morseDict[char.upper()]
        temp.append(morseChar)
    morse.append(' '.join(temp))
    temp.clear()
    print(f"'{text}' in morse code: {' '.join(morse)}")

def main():
    word = str(input("Enter a text: "))
    morseEncoder(word)

main()