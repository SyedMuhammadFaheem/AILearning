import random
class UAV:
    sensors=[]

    def __init__(self):
        self.sensors=[]
    
    def inputTemp(self):
        for i in range(9):
            self.sensors.append(random.uniform(20,55))
    
    def calAvg(self):
        sumTemp=0
        for temp in self.sensors:
            sumTemp+=temp
        avgTemp=sumTemp/9
        fahTemp=(avgTemp*1.8)+32
        print("The average temperature in fahrenheit is: ",fahTemp)


uavObj=UAV()
uavObj.inputTemp()
uavObj.calAvg()