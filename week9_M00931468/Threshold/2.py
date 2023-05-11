# /home/midev/Desktop/Python/CST1510/week9_M00931468/Threshold/les_Brown.txt

def capitalize(filename, new):
    allLines = []
    with open(filename,"r") as original,open(new,"a") as final :
        lines = original.readlines()
        for line in lines:
            for word in line.split():
            
                if "yourself" in word:
                    allLines.append(word)
                    continue
                elif "your" in word:
                    allLines.append(word)
                    continue
                elif "you" in word:
                    text = word.replace("you","YOU")
                    allLines.append(text)
                else:
                    allLines.append(word)
        newtext = ' '.join(allLines)    
        final.writelines(newtext)
    
                    

        


capitalize("/home/midev/Desktop/Python/CST1510/week9_M00931468/Threshold/les_Brown.txt","/home/midev/Desktop/Python/CST1510/week9_M00931468/Threshold/posiability.txt")