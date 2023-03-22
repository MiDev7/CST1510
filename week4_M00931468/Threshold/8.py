import math

def sqrtTable():
    print("Number\tSquare root")
    for index in range(0,20,2):
        print(f"{index}\t{round(math.sqrt(index),2)}")

sqrtTable()

        