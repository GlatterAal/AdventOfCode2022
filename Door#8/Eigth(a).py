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
    sum=0
    for i in range (0,len(arr)):
        for j in range (0, len(arr[i])):
            h=0
            if(i==0 or i==len(arr)-1 or j==0 or j==len(arr[i])-1):
                sum+=1
            else:
                current=arr[i][j]
                for k in range(i-1,-1,-1):
                    if(arr[k][j]>=current):
                        h+=1
                        break
                for k in range(i+1,len(arr)):
                    if(arr[k][j]>=current):
                        h+=1
                        break
                for k in range(j-1,-1,-1):
                    if(arr[i][k]>=current):
                        h+=1
                        break
                for k in range(j+1,len(arr[i])):
                    if(arr[i][k]>=current):
                        h+=1
                        break
                if(h<4):
                    sum+=1
    return sum
print(main("input.txt"))