# /home/midev/Desktop/Python/CST1510/week9_M00931468/Typical/python_zen.txt

def add_line(original, new):
    x = 0
    with open(original, "r") as first, open(new,"a") as second:
        for line in first:
            if x == 0:
                text= line
            else:
                text= f"{x}. {line}"
            second.write(text)
            x += 1

        
add_line("/home/midev/Desktop/Python/CST1510/week9_M00931468/Typical/python_zen.txt","/home/midev/Desktop/Python/CST1510/week9_M00931468/Typical/zen.txt")
