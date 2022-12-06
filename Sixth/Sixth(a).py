
def isMark(c1,c2,c3,c4):
    if(c1==c2 or c1==c3 or c1==c4 or c2==c3 or c2==c4 or c3==c4):
        return True
    return False

def main(file):
    f=open(file,"r")
    for line in f:
        for i in range(3,len(line)):
            if(not isMark(line[i],line[i-1],line[i-2],line[i-3])):
                print(i+1)
                break
            
print(main(r"C:\Users\Admin\Desktop\GitHubProjects\AdventOfCode2022\Sixth\input.txt"))

