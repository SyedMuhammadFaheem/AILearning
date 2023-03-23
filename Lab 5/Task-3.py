#Task 3
import numpy as np
def greedyBFS(source,graph,visited,cost,heuristics,goal,nodes):
    final_cost=0
    path=[]
    queue=[]
    queue.append(source)
    costs=[]
    while queue:
        curr_parent=queue.pop(0)
        visited[curr_parent]=True
        path.append(nodes[curr_parent])
        if curr_parent==goal:
            break
        for i in range(len(graph[curr_parent])):
            node=graph[curr_parent][i]
            if visited[node]==False:
                costs.append(heuristics[node])
        costs=sorted(costs)
        queue.clear()
        for i in range(len(costs)):
            queue.append(heuristics.index(costs[i]))
        if costs:
            costs.pop(0)
    for i in range(len(path)):
        if i+1<len(path):
            final_cost+=cost[(nodes.index(path[i]),nodes.index(path[i+1]))]
            
    return path,final_cost
                        
                         

def tree_init():
    graph=[[] for i in range(10)]
    visited=[False for i in range(10)]
    heuristics=[]
    nodes=['S','A','B','C','D','E','F','H','I','G']
    cost={}
    graph[0].append(1)
    graph[0].append(2)
    graph[1].append(3)
    graph[1].append(4)
    graph[2].append(5)
    graph[2].append(6)
    graph[5].append(7)
    graph[6].append(8)
    graph[6].append(9)
    heuristics.append(13)
    heuristics.append(12)
    heuristics.append(4)
    heuristics.append(7)
    heuristics.append(3)
    heuristics.append(8)
    heuristics.append(2)
    heuristics.append(4)
    heuristics.append(9)
    heuristics.append(0)
    cost[(0,1)]=3
    cost[(0,2)]=2
    cost[(1,3)]=4
    cost[(1,4)]=1
    cost[(2,5)]=3
    cost[(2,6)]=1
    cost[(5,7)]=5
    cost[(6,8)]=2
    cost[(6,9)]=3
    return graph,cost,heuristics,nodes,visited

source=0
goal=9
graph,cost,heuristics,nodes,visited=tree_init()
path,final_cost=greedyBFS(source,graph,visited,cost,heuristics,goal,nodes)
print('Path: ',path)
print('Final Cost: ',final_cost)