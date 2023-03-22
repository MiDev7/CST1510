totalStudNum = int(input("Enter the total number of students: "))

highestScore = 0
secondScore = 0
studentName =  ""
studentName2 =  ""
for index in range(1, totalStudNum + 1):
    studName = str(input("Enter student name: "))
    studScore = int(input("Enter student score: "))
    if studScore > secondScore:
        if secondScore > highestScore:
            highestScore = secondScore
            studentName = studName
        else:
            secondScore = studScore
            studentName2 = studName
        
    
print(f"{studentName} has the highest score, that is {highestScore}")
print(f"{studentName2} has the highest score, that is {secondScore}")