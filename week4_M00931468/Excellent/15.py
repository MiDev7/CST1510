def pyramidalNum(row):
    for index in range(1, row+1):
        print(" "*(row-index)*2, end="")
        for num2 in range(1, index+1):
            print(num2, end=" ")
        for num2 in range(index-1, 0, -1):
            print(num2, end=" ")
        print()


def main():
    num = int(input("Please enter the total number of row: "))
    pyramidalNum(num)

main()