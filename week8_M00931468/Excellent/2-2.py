import math

def binaryToHexadecimal(binary):
    decimal = 0
    decimalPerBit = 0
    power = 0
    BASE = 16

    integerBinary = int(binary)
    for index in range(0,len(binary)):
        remainder = integerBinary % 10
        decimalPerBit = remainder * math.pow(BASE,power)
        power +=1
        integerBinary = integerBinary // 10
        decimal += decimalPerBit

    return int(decimal)

def main():

    while True:
        try:
            binary = input("Enter a binary number: ")
            int(binary, 2)
        except:
            print("Binary number should consists of only 0 and 1, Please try again ...")
            continue
        else:
            break
    # print(binaryToDecimal(binary))

    print(f"Here is your binary number in decimal: {binaryToHexadecimal('10001')}")


main()
