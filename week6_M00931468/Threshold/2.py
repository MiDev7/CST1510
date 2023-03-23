import random

def random_throws():
    throws = []

    for index in range(0,7):
        throws.append(random.randint(1,6))

    # Normal list
    print(f"This is the normal list: {throws}")
    # Shuffle list
    random.shuffle(throws)
    print(f"This is the shuffled list: {throws}")

    # Sorted list
    throws.sort(reverse=True)
    print(f"This is the sorted, descending list: {throws}")

    # Count occurence

    print(f"1 occurence is {throws.count(1)}")
    print(f"2 occurence is {throws.count(2)}")
    print(f"3 occurence is {throws.count(3)}")
    print(f"4 occurence is {throws.count(4)}")
    print(f"5 occurence is {throws.count(5)}")
    print(f"6 occurence is {throws.count(6)}")

def main():
    random_throws()

main()