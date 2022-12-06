def main(file):
    f=open(file,"r")
    #arr=[["Z","N"],["M","C","D"],["P"]] 
    arr=[["G","T","R","W"],["G","C","H","P","M","S","V","W"],["C","L","T","S","G","M"],["J","H","D","M","W","R","F"],["P","Q","L","H","S","W","F","J"],["P","J","D","N","F","M","S"],["Z","B","D","F","G","C","S","J"],["R","T","B"],["H","N","W","L","C"]]
    for line in f:
        s=line.replace("move ","").replace("from ","").replace("to ","").replace("\n","").split(" ")
        a1=[]
        arr1=arr[int(s[1])-1]
        arr2=arr[int(s[2])-1]
        for i in range(0,int(s[0])):
            a1.append(arr1[-1])
            arr1.pop(-1)
        a1=a1[::-1]
        for i in range(0,len(a1)):
            arr2.append(a1[i])
        arr[int(s[1])-1]=arr1
        arr[int(s[2])-1]=arr2
    s=""
    for a in arr:
        s=s+a[-1]
    return s
print(main(r"input.txt"))  