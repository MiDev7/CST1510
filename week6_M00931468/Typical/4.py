import random

def randomListSelectionGen():
    selection = [random.randint(1,49) for index in range(0,6)]
    selection.sort()
    print(selection)
    return selection


def main():
    randomListSelectionGen()

main()