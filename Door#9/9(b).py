
def main(file):
    f=open(file,"r")
    arr=[[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]
    oldArr=[[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]
    allNineth=[[1,1]]
    for line in f:
        line=line.replace("\n","").split(" ")
        if(line[0]=="U"):
            for i in range(int(line[1])):
                for e in range(len(arr)-1):
                    oldArr[e][0]=arr[e][0]
                    oldArr[e][1]=arr[e][1]
                    arr[e][1]+=1
                    if(abs(arr[e][1]-arr[e-1][1])==2):
                        arr[e-1][0]=oldArr[e][0]
                        arr[e-1][1]=oldArr[e][1]
                        if(e==len(arr)-1):
                            help=0
                            for k in allNineth:
                                if(arr[e-1][0]==k[0]):
                                    if(arr[e-1][1]==k[1]):
                                        help+=1
                            if(help==0):
                                allNineth.append([arr[e-1][0],arr[e-1][1]])
        if(line[0]=="D"):
            for i in range(int(line[1])):
                for e in range(len(arr)-1):
                    oldArr[e][0]=arr[e][0]
                    oldArr[e][1]=arr[e][1]
                    arr[e][1]-=1
                    if(abs(arr[e][1]-arr[e-1][1])==2):
                        arr[e-1][0]=oldArr[e][0]
                        arr[e-1][1]=oldArr[e][1]
                        if(e==len(arr)-1):
                            help=0
                            for k in allNineth:
                                if(arr[e-1][0]==k[0]):
                                    if(arr[e-1][1]==k[1]):
                                        help+=1
                            if(help==0):
                                allNineth.append([arr[e-1][0],arr[e-1][1]])
        if(line[0]=="R"):
            for i in range(int(line[1])):
                for e in range(len(arr)-1):
                    oldArr[e][0]=arr[e][0]
                    oldArr[e][1]=arr[e][1]
                    arr[e][0]+=1
                    #print(abs(arr[e][0]-arr[e-1][0]))
                    if(abs(arr[e][0]-arr[e-1][0])==2):
                        print(e)
                        arr[e-1][0]=oldArr[e][0]
                        arr[e-1][1]=oldArr[e][1]
                        if(e==len(arr)-1):
                            help=0
                            for k in allNineth:
                                if(arr[e-1][0]==k[0]):
                                    if(arr[e-1][1]==k[1]):
                                        help+=1
                            if(help==0):
                                allNineth.append([arr[e-1][0],arr[e-1][1]])
                #print(arr,oldArr)
        if(line[0]=="L"):
            for i in range(int(line[1])):
                for e in range(len(arr)-1):
                    oldArr[e][0]=arr[e][0]
                    oldArr[e][1]=arr[e][1]
                    arr[e][0]-=1
                    if(abs(arr[e][0]-arr[e-1][0])==2):
                        arr[e-1][0]=oldArr[e][0]
                        arr[e-1][1]=oldArr[e][1]
                        if(e==len(arr)-1):
                            help=0
                            for k in allNineth:
                                if(arr[e-1][0]==k[0]):
                                    if(arr[e-1][1]==k[1]):
                                        help+=1
                            if(help==0):
                                allNineth.append([arr[e-1][0],arr[e-1][1]])
                    
    return len(allNineth)
print(main("test(b).txt"))