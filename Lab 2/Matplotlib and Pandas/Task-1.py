#Task 1
import numpy as np
import matplotlib.pyplot as plt
xPoints=np.array([1,2,3,4,5])
yPoints=np.array([10,20,30,40,50])
xTempPoints=np.array([-1,-2,-3,-4,-5])
yTempPoints=np.array([10,20,30,40,50])
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(xPoints,yPoints,linestyle='dotted')
plt.plot(xTempPoints,yTempPoints)
plt.show()