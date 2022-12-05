import math

def main(file):
    max=0
    current=0
    f=open(file,"r")
    for line in f:
        if(len(line)<=1):
            if(current>max):
                max=current
            current=0
        else:
            current+=int(line)
    if(current>max):
        max=current
    return max

print(main(r"C:\Users\pc\Desktop\Github\AdventOfCode2022\First\test.txt"))
