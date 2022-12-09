
def main(file):
    f=open(file,"r")
    H=[1,1]
    T=[1,1]
    oldH=[1,1]
    allT=[[1,1]]
    for line in f:
        line=line.replace("\n","").split(" ")
        if(line[0]=="U"):
            for i in range(int(line[1])):
                oldH[0]=H[0]
                oldH[1]=H[1]
                H[1]=H[1]+1
                if(abs(H[1]-T[1])==2):
                    T[0]=oldH[0]
                    T[1]=oldH[1]
                    help=0
                    for e in allT:
                        if(T[0]==e[0]):
                            if(T[1]==e[1]):
                                help+=1
                    if(help==0):
                        allT.append([T[0],T[1]])
        if(line[0]=="D"):
            for i in range(int(line[1])):
                oldH[0]=H[0]
                oldH[1]=H[1]
                H[1]=H[1]-1
                if(abs(H[1]-T[1])==2):
                    T[0]=oldH[0]
                    T[1]=oldH[1]
                    help=0
                    for e in allT:
                        if(T[0]==e[0]):
                            if(T[1]==e[1]):
                                help+=1
                    if(help==0):
                        allT.append([T[0],T[1]])
        if(line[0]=="L"):
            for i in range(int(line[1])):
                oldH[0]=H[0]
                oldH[1]=H[1]
                H[0]=H[0]-1
                if(abs(H[0]-T[0])==2):
                    T[0]=oldH[0]
                    T[1]=oldH[1]
                    help=0
                    for e in allT:
                        if(T[0]==e[0]):
                            if(T[1]==e[1]):
                                help+=1
                    if(help==0):
                        allT.append([T[0],T[1]])
        if(line[0]=="R"):
            for i in range(int(line[1])):
                oldH[0]=H[0]
                oldH[1]=H[1]
                H[0]=H[0]+1
                if(abs(H[0]-T[0])==2):
                    T[0]=oldH[0]
                    T[1]=oldH[1]
                    help=0
                    for e in allT:
                        if(T[0]==e[0]):
                            if(T[1]==e[1]):
                                help+=1
                    if(help==0):
                        allT.append([T[0],T[1]])
    return len(allT)
print(main("input.txt"))