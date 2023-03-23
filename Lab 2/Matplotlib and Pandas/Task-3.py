#Task 3
import pandas as pd
data = {
    'duration' : [60,60,60,45,45],
    'Pulse' : [110,117,103,109,117],
    'Max Pulse' : [130,145,135,175,148],
    'Calories' : [409.1,479,340,282.4,406]
}
dataNew = {
    'duration' : [60,60,60,45,45],
    'Pulse' : [110,117,103,109,117],
    'Max Pulse' : [130,145,135,175,148],
    'Calories' : [409.1,479,340,282.4,406]
}
file=pd.DataFrame(data)
file.to_csv("Test.csv",index=False)
newFile=pd.read_csv("Test.csv")
print(newFile)
df=pd.DataFrame(dataNew)
df.to_csv("Test.csv",mode='a',index=False,header=False)
print(pd.read_csv("Test.csv"))