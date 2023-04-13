def DecimalToBinary(decimal):
    decimal = int(decimal)
    binary = ""
    while True:
        remainder = decimal % 2
        decimal = decimal // 2

        if remainder != 0:
            binary+="1"
        elif  decimal == 0:
            break
        elif remainder == 0:
            binary+="0"   

    return binary[::-1]

def main():

    while True:
        try:
            decimal = input("Enter a decimal number: ")
            int(decimal, 10)
        except:
            print("Decimal number should consists of only 0 and 9, Please try again ...")
            continue
        else:
            break
    print(DecimalToBinary(decimal))

    print(DecimalToBinary(10))

main()
