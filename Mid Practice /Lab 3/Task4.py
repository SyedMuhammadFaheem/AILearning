import random
class Model:
    environment=[]
    path=[]
    def __init__(self,n,m):
        self.environment=[['' for j in range(m)] for i in range(n)]
        self.path=[]
   
    def setEnvironment(self):
        choices=['D','B','C']
        for i in range(len(self.environment)):
            for j in range(len(self.environment[i])):
                self.environment[i][j]=random.choice(choices)
        self.environment[0][0]='D'
    
    def runEnvironment(self):
        i,j=0,0
        while True:
            if self.environment[i][j]=='C':
                continue
            self.path.append((i,j))
            self.environment[i][j]='C'
            for row in self.environment:
                print(row)
            print('\n\n')
            if i>0 and self.environment[i-1][j]=='D':
                i-=1
                continue
            elif i<len(self.environment) and self.environment[i+1][j]=='D':
                i+=1
                continue
            elif j>0 and self.environment[i][j-1]=='D':
                j-=1
                continue
            elif j<len(self.environment[i]) and self.environment[i][j+1]=='D':
                j+=1
                continue
            else:
                break
        self.printPath()

    def printPath(self):
        print(self.path)


modelObj=Model(10,5)
modelObj.setEnvironment()
modelObj.runEnvironment()