def isSublist(largerlist, smallerlist):
    if len(smallerlist) == 0:
        return True
    # The second argument in the range "(len(largerlist) - len(smallerlist) + 1)" is mathematical equation which is used to find the perfect amount time the batching of the subList. For example: Large List is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], and small List is [2, 3, 4]. There respective length is 10 and 3. The result of the operation is (10 - 3) = 7. The plus is used since the last number in a range is always excluded. Therefore, the second argument of range is 8. The for loop will iterate 8 times
    for index in range(0,(len(largerlist) - len(smallerlist) + 1)):
        # The if condition down below uses list slicing to slice the large array to have the same length as the small one. For instance: index = 0 and Largelist[0:3]. The result of that slicing is now [1,2,3]. After that it is then evaluated with this smallerList = [2,3,4].
        if largerlist[index:index + len(smallerlist)] == smallerlist:
            return True
    return False


largerlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
smallerlist1 = [2, 3, 4]
smallerlist2 = [2, 4, 3]
smallerlist3 = [11, 12]
smallerlist4 = []
print(isSublist(largerlist, smallerlist1))  # True
print(isSublist(largerlist, smallerlist2))  # False
print(isSublist(largerlist, smallerlist3))  # False
print(isSublist(largerlist, smallerlist4))  # False






