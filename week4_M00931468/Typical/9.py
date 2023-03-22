def revPattern(row):
    for index in reversed(range(1,row + 1)):
        for num in reversed(range(1,index + 1)) :
            print(num, end = " ")
        print("\n")

def main():
    row = int(input("Enter number of row: "))
    revPattern(row)

main()