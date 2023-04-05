import math

def binaryToHexadecimal(binary):
    decimal = 0
    decimalPerBit = 0
    power = 0
    for bit in reversed(binary):
        decimalPerBit = int(bit) * math.pow(16,power)
        decimal = decimal + decimalPerBit
        power+=1

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

    print(binaryToHexadecimal("10001"))


main()
