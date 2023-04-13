import math

def binaryToDecimal(binary):
    decimal = 0
    decimalPerBit = 0
    power = 0
    for bit in reversed(binary):
        decimalPerBit = int(bit) * math.pow(2,power)
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
    print(int(binary,2))
    print(f'10001 in decimal is: {binaryToDecimal("10001")}')


main()
