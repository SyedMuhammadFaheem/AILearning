#Task 6
import queue as q
import numpy as np
import copy
def solve_8_puzzle_problem(initial,goal):
    queue=q.PriorityQueue()
    queue.put((0,initial,[]))
    visited=[[] for i in range(9)]
    while not queue.empty():
        curr_cost,curr_state,path=queue.get()
        if curr_state==goal:
            return path
        visited.append(curr_state)
        for adjacent in get_neighbour_states(curr_state):
            if adjacent not in visited:
                cost=len(path)+1+man_distance(adjacent,goal)
                queue.put((cost,adjacent,path+[adjacent]))
    return None          
    
def man_distance(state_1,state_2):
    dist=0
    for i in range(9):
        temp1=list(zip(*np.where(np.array(state_1)==i)))
        x1,y1=temp1[0]
        temp2=list(zip(*np.where(np.array(state_2)==i)))
        x2,y2=temp2[0]
        dist+= abs(x1-x2)+abs(y1-y2)
    return dist
    
def get_neighbour_states(state):
    neighbours=[]
    temp1=list(zip(*np.where(np.array(state)==0)))
    empty_index=temp1[0]
    x=empty_index[0]
    y=empty_index[1]
    if empty_index not in [(0,0),(0,1),(0,2)]:
        adj=copy.deepcopy(state)
        adj[x][y],adj[x-1][y]=adj[x-1][y],adj[x][y]
        neighbours.append(adj)
    if empty_index not in [(2,0),(2,1),(2,2)]:
        adj=copy.deepcopy(state)        
        adj[x][y],adj[x+1][y]=adj[x+1][y],adj[x][y]       
        neighbours.append(adj)
    if empty_index not in [(0,0),(1,0),(2,0)]:
        adj=copy.deepcopy(state)
        adj[x][y],adj[x][y-1]=adj[x][y-1],adj[x][y]
        neighbours.append(adj)
    if empty_index not in [(0,2),(1,2),(2,2)]:
        adj=copy.deepcopy(state)
        adj[x][y],adj[x][y+1]=adj[x][y+1],adj[x][y]
        neighbours.append(adj)
    
    return neighbours 
    
initial=[[7,2,4],[5,0,6],[8,3,1]]
goal=[[0,1,2],[3,4,5],[6,7,8]]
print('Initial State: ')
for row in initial:
    print(row)
print()
path=solve_8_puzzle_problem(initial,goal)
i=0
for paths in path:
    if i+1==len(path):
        print('Final State')
    else:
        print('Transition',i+1)
    i+=1
    for row in paths:
        print(row)
        
    print('\n')