#Task6
import numpy as np
n=5
nodes=['FAST NU','Karsaz','Gulshan','Korangi','Saddar']
adj_mat=[[0,15,30,20,-1],[15,0,8,10,10],[30,8,0,22,20],[20,10,22,0,10],[-1,10,20,10,0]]
dist=[9999 for item in range(5)]
dist[0]=0
visited=[]
u=0

while len(visited)<n:
    if u not in visited:
        visited.append(u)
    for i in range(n):
        if adj_mat[u][u]<adj_mat[u][i]+adj_mat[u][u]:
            dist[i]=min(adj_mat[u][u]+adj_mat[u][i],dist[i])
            adj_mat[i][i]=dist[i]
    u+=1
source=nodes[0]
for item in nodes:
    if item != source:
        print(str(source) + ' to ' + item + ': ' + str(dist[nodes.index(item)]) + ' km')