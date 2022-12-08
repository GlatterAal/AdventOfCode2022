class Directory():
    def __init__(self,name,parent) -> None:
        self.name=name
        self.parent=parent
        self.files=[]
        self.directorys=[]
    def addFile(self, file):
        self.files.append(file)
    def addDir(self,dir):
        self.directorys.append(dir)
    def getSize(self):
        ret=0
        for f in self.files:
            ret+=int(f)
        for dir in self.directorys:
            ret+=dir.getSize()
        return ret
    def getName(self):
        return self.name
    def getDir(self,dirName):
        for dir in self.directorys:
            if(dir.getName()==dirName):
                return dir
        return self
    def getParentDir(self):
        return self.parent
    def getAllUnderTenThousand(self):
        l=[]
        for dir in self.directorys:
            if(not dir.getDirectorys()):
                pass
    

def main(f):
    f=open(f,"r")
    path=Directory("/",None)
    allDirs=[path]
    currentDir=path
    for line in f:
        line=line.replace("\n","").split(" ")
        if(line[0]=="$"):
            if(line[1]=="cd"):
                if(line[2]==".."):
                    currentDir=currentDir.getParentDir()
                else:
                    currentDir=currentDir.getDir(line[2])
            elif(line[1]=="ls"):
                continue
        elif(line[0]=="dir"):
            elem=Directory(line[1],currentDir)
            currentDir.addDir(elem)
            allDirs.append(elem)
        else:
            currentDir.addFile(line[0])
    work=[]
    min=70000000
    cur=path
    freeSpace=70000000-path.getSize()
    hasToBeDeleted=30000000-freeSpace
    for dir in allDirs:
        if(dir.getSize()>=hasToBeDeleted):
            work.append(dir)
    for i in work:
        if(i.getSize()<min):
            min=i.getSize()
            cur=i
    return cur.getSize()
    
print(main("input.txt"))

