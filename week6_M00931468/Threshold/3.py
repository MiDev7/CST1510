import random

# Create a 3x3 matrix with random numbers between 1 and 10
matrix = [[random.randint(1, 10) for j in range(4)] for i in range(4)]

def sum_row(matrix,row_index):
    sumRow= sum(matrix[row_index])
    print(f"The sum of the {row_index+1} is {sumRow}\n")

def sumOfEachRow(matrix):
    for index in range(len(matrix)):
        print(f"The sum of the {index+1} row is {sum(matrix[index])}")



print(matrix)
def main():
    sum_row(matrix,1)
    sumOfEachRow(matrix)

main()