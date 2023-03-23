import random



def countRange1(list,min,max):
    return len([item for item in list if item >= min and item < max])


def countRange2(list,min,max):
    count = 0
    for item in list:
        if item >= min and item < max:
            count += 1 
    return count

def main():
    randList = [random.randint(1,50) for i in range(random.randint(2,9))]
    print(randList)
    print(countRange1(randList,15,30))
    print(countRange2(randList,15,30))

main()