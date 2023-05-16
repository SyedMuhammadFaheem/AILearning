import random
class reflexEnv:
    frontCam=[]
    rearCam=[]
    leftCam=[]
    rightCam=[]

    def __init__(self):
        self.frontCam=('front',random.randint(0,10))
        self.rearCam=('rear',random.randint(0,10))
        self.leftCam=('left',random.randint(0,10))
        self.rightCam=('right',random.randint(0,10))
    
    def actionsTaken(self,camObj):
        if camObj[0]=='front' and camObj[1]<=8:
            print('Apply brakes automatically!')
        elif camObj[0]=='left' and camObj[1]<=2:
            print('Move to the right lane!')
        elif camObj[0]=='right' and camObj[1]<=2:
            print('Move to the left lane!')
        elif camObj[0]=='rear' and camObj[1]<=5:
            print('Apply brakes when parking the car!')
    
    def printCamStats(self):
        print('Front Cam: ',self.frontCam)
        print('Rear Cam: ',self.rearCam)
        print('Right Cam: ',self.rightCam)
        print('Left Cam: ',self.leftCam)
    
    def runEnvironment(self):
        self.actionsTaken(self.frontCam)
        self.actionsTaken(self.rearCam)
        self.actionsTaken(self.leftCam)
        self.actionsTaken(self.rightCam)

reflexObj=reflexEnv()
reflexObj.printCamStats()
reflexObj.runEnvironment()
        