#Task4
import numpy as np
import random
m=int(input("Enter the rows: "))
n=int(input("Enter the columns: "))
env=np.empty(shape=(m,n),dtype=str)
leg=['C','B','D']
env[0][0]='D'
for i in range(m):
    for j in range(n):
        if env[i][j]=='':
            if i==0 and j==0:
                continue
            env[i][j]=leg[random.randint(0,2)]

path=[]
i,j=0,0
while True:
    if env[i][j]=='C':
        continue
    path.append((i, j))
    env[i][j] = "C"
    print(env,'\n')
    if i>0 and env[i-1][j] == "D":
        i-=1
        continue
    if i<n-1 and env[i+1][j] == "D":
        i+=1
        continue
    if j>0 and env[i][j-1] == "D":
        j-=1
        continue
    if j<m-1 and env[i][j+1] == "D":
        j+=1
    else:
        break
        
print("The path taken by the vacuum cleaner:", path)