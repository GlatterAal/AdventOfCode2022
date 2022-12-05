def getDoubles(s1,s2,s3):
    ret=""
    for e in s1:
        for j in s2:
            for k in s3:
                if(e==j==k):
                    ret=k
                    break
    return ret

def getValue(n):
    if(ord(n)>90):
        return ord(n)-96
    else:
        return ord(n)-38

def main(file):
    f=open(file,"r")
    max=0
    s1=""
    s2=""
    s3=""
    i=1
    for line in f:
        if(i==1):
            s1=line.replace("\n","")
        if(i==2):
            s2=line.replace("\n","")
        if(i==3):
            s3=line.replace("\n","")
            max+=getValue(getDoubles(s1,s2,s3))
            i=0
        i+=1
    return max

print(main(r"C:\Users\pc\Desktop\Github\AdventOfCode2022\Third\input.txt"))