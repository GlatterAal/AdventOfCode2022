def getEquvalent(n):
    if(n =="X"):
        return "A"
    if(n =="Y"):
        return "B"
    if(n =="Z"):
        return "C"
    else:
        return "ERROR 01"

def getRes(a,b):
    if(a==b):
        return 3
    if (a=="A"):
        if(b=="B"):
            return 6
        else:
            return 0
    if(a=="B"):
        if(b=="C"):
            return 6
        else:
            return 0
    if(a=="C"):
        if(b=="A"):
            return 6
        else:
            return 0

def getVal(b):
    if(b=="A"):
        return 1
    if(b=="B"):
        return 2
    else:
        return 3
def main(file):
    f=open(file,"r")
    max=0
    for line in f:
        input=line.split(" ")
        a=input[0]
        b=getEquvalent(input[1].replace("\n",""))
        res=getRes(a,b)
        val=getVal(b)
        max+=res+val
    return max
        
print(main(r"C:\Users\pc\Desktop\Github\AdventOfCode2022\Second\input.txt"))