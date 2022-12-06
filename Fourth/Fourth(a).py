def main(file):
    f=open(file,"r")
    max=0
    for line in f:
        arr=line.split(",")
        s1=int(arr[0].split("-")[0])
        e1=int(arr[0].split("-")[1])
        s2=int(arr[1].split("-")[0])
        e2=int(arr[1].split("-")[1])
        if((s1<=s2 and e1>=e2) or (s2<=s1 and e2>=e1)):
            max+=1
    return max

print(main(r"input.txt"))         