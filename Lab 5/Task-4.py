#Task 4
import numpy as np
def a_star(source,graph,visited,cost,heuristics,goal,nodes):
    final_cost=0
    path={}
    queue=[]
    queue.append((source,-1))
    costs=[0 for i in range(10)]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            costs[graph[i][j]]=cost[(i,graph[i][j])]+costs[i]
    function=[]                  
    while queue:
        curr_parent,par_parent=queue.pop(0)
        visited[curr_parent]=True
        if curr_parent==goal:
            path[nodes[curr_parent]]=nodes[par_parent]
            break
        if curr_parent==source:
            path[nodes[curr_parent]]=par_parent
        else:
            path[nodes[curr_parent]]=nodes[par_parent]
        for i in range(len(graph[curr_parent])):
            node=graph[curr_parent][i]
            if visited[node]==False:
                function.append(costs[node]+heuristics[node])
                queue.append((node,curr_parent))
        temp1=np.array(function)
        temp2=np.array(queue)
        sort=np.argsort(temp1)
        function=list(temp1[sort])
        queue=list(temp2[sort])
        function=sorted(function)
        if function:
            function.pop(0)
    final_cost=0
    final_path=[]
    key=nodes[goal]
    while key!=-1:
        final_path.insert(0,key)
        if path[key]!=-1:
            final_cost+=cost[(nodes.index(path[key]),nodes.index(key))]
        key=path[key]       
    return final_path,final_cost
                        
                         

def tree_init():
    graph=[[] for i in range(6)]
    visited=[False for i in range(6)]
    heuristics=[]
    nodes=['S','A','B','C','D','G']
    cost={}
    graph[0].append(1)
    graph[0].append(5)
    graph[1].append(2)
    graph[1].append(3)
    graph[2].append(4)
    graph[3].append(4)
    graph[3].append(5)
    graph[4].append(5)
    heuristics.append(5)
    heuristics.append(3)
    heuristics.append(4)
    heuristics.append(2)
    heuristics.append(6)
    heuristics.append(0)
    cost[(0,1)]=1
    cost[(0,5)]=10
    cost[(1,2)]=2
    cost[(1,3)]=1
    cost[(2,4)]=5
    cost[(3,4)]=3
    cost[(3,5)]=4
    cost[(4,5)]=6
    return graph,cost,heuristics,nodes,visited

source=0
goal=5
graph,cost,heuristics,nodes,visited=tree_init()
path,final_cost=a_star(source,graph,visited,cost,heuristics,goal,nodes)
print('Path: ',path)
print('Final Cost: ',final_cost)
    