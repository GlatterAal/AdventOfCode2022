def getArr(f):
    arr=[]
    for line in f:
        line=line.replace("\n","")
        h=[]
        for i in line:
            h.append(int(i))
        arr.append(h)
    return arr

def main(file):
    f=open(file,"r")
    arr=getArr(f)
    maxScore=0
    for i in range (0,len(arr)):
        for j in range (0, len(arr[i])):
            score=1
            if(i==0 or i==len(arr)-1 or j==0 or j==len(arr[i])-1):
                score=1
            else:
                current=arr[i][j]
                ks=[]
                steps=0
                for k in range(i-1,-1,-1):
                    steps+=1
                    if(arr[k][j]>=current):
                        score*=steps
                        ks.append(steps)
                        steps=0
                        break
                else:
                    score*=steps
                    ks.append(steps)
                    steps=0
                for k in range(i+1,len(arr)):
                    steps+=1
                    if(arr[k][j]>=current):
                        score*=steps
                        ks.append(steps)
                        steps=0
                        break
                else:
                    score*=steps
                    ks.append(steps)
                    steps=0
                for k in range(j-1,-1,-1):
                    steps+=1
                    if(arr[i][k]>=current):
                        score*=steps
                        ks.append(steps)
                        steps=0
                        break
                else:
                    score*=steps
                    ks.append(steps)
                    steps=0
                for k in range(j+1,len(arr[i])):
                    steps+=1
                    if(arr[i][k]>=current):
                        score*=steps
                        ks.append(steps)
                        steps=0
                        break
                else:
                    score*=steps
                    ks.append(steps)
                    steps=0
                if(score>maxScore):
                    maxScore=score
    return maxScore
print(main("input.txt"))