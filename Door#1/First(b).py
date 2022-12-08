import math

def main(file):
    max1=0
    max2=0
    max3=0
    current=0
    f=open(file,"r")
    for line in f:
        if(len(line)<=1):
            if(current>max1):
                max3=max2
                max2=max1
                max1=current
            elif(current>max2):
                max3=max2
                max2=current
            elif(current>max3):
                max3=current
            current=0
        else:
            current+=int(line)
    if(current>max1):
        max3=max2
        max2=max1
        max1=current
    elif(current>max2):
        max3=max2
        max2=current
    elif(current>max3):
        max3=current
    return max1+max2+max3

print(main(r"input.txt"))