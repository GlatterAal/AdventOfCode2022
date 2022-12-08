def isMark(arr):
    arr2=[]
    for e in arr:
        for j in arr2:
            if(e==j):
                return True
        arr2.append(e)
    return False

def main(file):
    f=open(file,"r")
    for line in f:
        for i in range(13,len(line)):
            arr=[]
            for j in range(0,14):
                arr.append(line[i-j])
            if(not isMark(arr)):
                s=""
                for k in arr[::-1]:
                    s=s+k
                print(s)
                break
            
print(main(r"input.txt")) 