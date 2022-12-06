def getDoubles(s):
    mid=int((len(s))/2)
    s1=s[:mid]
    s2=s[mid:]
    ret=[]
    for e in s1:
        for j in s2:
            if(e==j):
                ret.append(e)
                s1=s1.replace(e,"",s1.count(e))
                s2=s2.replace(e,"",s2.count(e))
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
    for line in f:
        character=getDoubles(line.replace("\n",""))
        for e in character:
            max+=getValue(e)
    return max

print(main(r"input.txt")) 