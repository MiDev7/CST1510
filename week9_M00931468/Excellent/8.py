def read_csv_file(filename):
    total = 0
    with open(filename,"r") as csv:
        lines = csv.readlines()
        for index in range(len(lines)):
            sumPerLine = 0
            array = lines[index].split(",")

            if  index == 0:
                continue
            if index == 1:
                for index in range(len(array)):
                    if index == 0:
                        continue
                        
                    value = array[index].strip()
                    if value == '':
                        continue

                    value = int(value)
                    if index == 1:
                        value = value * 0.5
                        sumPerLine += value
                    if index == 5:
                        value = value * 0.5
                        sumPerLine += value

                total += sumPerLine
            if index == 2:
                for index in range(len(array)):
                    if index == 0:
                        continue
                        
                    value = array[index].strip()
                    if value == '':
                        continue

                    value = int(value)
                    if index == 1:
                        value = value * 0.4
                        sumPerLine += value
                    if index == 2:
                        value = value * 0.1
                        sumPerLine += value
                    if index == 3:
                        value = value * 0.1
                        sumPerLine += value
                    if index == 4:
                        value = value * 0.1
                        sumPerLine += value
                    if index == 5:
                        value = value * 0.3
                        sumPerLine += value

                total += sumPerLine

            if index == 3:
                for index in range(len(array)):
                    if index == 0:
                        continue
                        
                    value = array[index].strip()
                    if value == '':
                        continue

                    value = int(value)
                    if index == 1:
                        value = value * 0.4
                        sumPerLine += value
                    if index == 2:
                        value = value * 0.2
                        sumPerLine += value
                    if index == 5:
                        value = value * 0.4
                        sumPerLine += value

                total += sumPerLine

            if index == 4:
                for index in range(len(array)):
                    if index == 0:
                        continue
                        
                    value = array[index].strip()
                    if value == '':
                        continue
                    value = int(value)
                    if index == 1:
                        value = value * 0.5
                        sumPerLine += value
                    if index == 2:
                        value = value * 0.1
                        sumPerLine += value
                    if index == 5:
                        value = value * 0.4
                        sumPerLine += value

                total += sumPerLine


    result = ((total / 400))*100
    print(f"Your result is {result}")

    if result >= 71 and result <= 100:
        print("Congrats!!!, you are in First Class")
    
    elif result >= 61 and result <= 70:
        print("Congrats!!!, you are in Upper Second class")
    
    elif result >= 51 and result <= 60:
        print("Congrats!!!, you are in Lower Second  class")

    elif result >= 41 and result <= 50:
        print("Congrats!!!, you are in Third class ")
    
    elif result <= 40 and result >= 0:
        print("Unfortunately you failed, try again next year")


read_csv_file("/home/midev/Desktop/Python/CST1510/week9_M00931468/Excellent/greats_20_21.csv")