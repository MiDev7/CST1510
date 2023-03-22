def multiplication(table):
    for index in range(0,10):
        print(f"{index} x {table} = {index * table}")

def main():
    numTable = int(input("Enter a number for multiplication:"))
    multiplication(numTable)

main()