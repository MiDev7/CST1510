def isSublist(larger, smaller):
    if len(smaller) == 0:
        return True
    for index in range(0,(len(larger) - len(smaller) + 1)):
        if larger[index:index + len(smaller)] == smaller:
            return True
    return False


larger = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
smaller1 = [2, 3, 4]
smaller2 = [2, 4, 3]
smaller3 = [11, 12]

print(isSublist(larger, smaller1))  # True
print(isSublist(larger, smaller2))  # False
print(isSublist(larger, smaller3))  # False





