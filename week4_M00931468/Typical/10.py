totalStudNum = int(input("Enter the total number of students: "))

highestScore = 0
studentName =  ""
for index in range(1, totalStudNum + 1):
    studName = str(input("Enter student name: "))
    studScore = int(input("Enter student score: "))
    if studScore > highestScore:
        highestScore = studScore
        studentName = studName
    
print(f"{studentName} has the highest score, that is{highestScore}")