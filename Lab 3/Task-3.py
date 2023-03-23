#Task3
import numpy as np
import random
temp=[]
for i in range(9):
    temp.append(random.uniform(-2, 45))
temp=np.array(temp)
print("Temperature in Celsius: ",temp,"\n")
temp=temp*1.8+32
print("Temperature in Fahrenheit: ",temp,"\n")
print("Average: ",sum(temp)/9)