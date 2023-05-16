import random
from math import sqrt
class ICE:
    environment=[]
    distancePoints=[]
    def __init__(self,n):
        self.environment=[['' for i in range(n)] for i in range(n)]
        self.distancePoints=[]
    
    def euclideanDistance(self,x2,y2):
        distance=sqrt((((x2-4)**2)+((y2-0)**2)))
        return distance

    def setReferencePoint(self):
        if self.environment[4][0]=='':
            self.environment[4][0]='R'

    def placeRobotPositions(self):
        robots=['A','B','C','D','N']
        j=0
        while True:
            roboChoice=robots[j]
            randX=random.randint(0,len(self.environment)-1)
            randY=random.randint(0,len(self.environment)-1)
            if self.environment[randX][randY]=='':
                self.environment[randX][randY]=roboChoice
                j+=1
            if j==len(robots):
                break
    
    def calculateDistance(self,x2,y2):
        self.distancePoints.append(self.euclideanDistance(x2,y2))
    
    def runEnvironment(self):
        self.setReferencePoint()
        self.placeRobotPositions()
        for i in range(len(self.environment)):
            for j in range(len(self.environment[i])):
                if self.environment[i][j]!='' and self.environment[i][j]!='R':
                    self.calculateDistance(i,j)
    
    def printDistance(self):
        print(self.distancePoints)


iceObj=ICE(10)
iceObj.runEnvironment()
iceObj.printDistance()

    