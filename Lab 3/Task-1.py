#Task1
import numpy as np
import random as r
import math

def distance(pos,x2,y2):
    return math.sqrt((pos[0] - pos[1])**2 + (x2 - y2)**2)

n=int(input("Enter the no. of locations: "))
env = np.empty(shape=(n,n),dtype=str)
env[4][0]='R'
robo_names=['A','B','C','D','N']
j=0
for i in range(0,5):
    x=r.randint(0,n-1)
    y=r.randint(0,n-1)
    if env[x][y]=='':
        env[x][y]=robo_names[j]
        j+=1
    else:
        j-=1
print(env)
r_pos=[4,0]
res=[]
for i in range(n):
    for j in range(n):
        if env[i][j] in robo_names:
            res.append(distance(r_pos,i,j))
print("\nEuclidean Distance among all given robots: ",res)