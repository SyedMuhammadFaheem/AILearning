#Task 5
import numpy as np
from queue import PriorityQueue
def man_distance(x1,y1):
    dist=0   
    dist= abs(x1-0)+abs(y1-10)
    return dist

def man_distance_source(x1,y1,x2,y2):
    dist=0   
    dist= abs(x1-x2)+abs(y1-y2)
    return dist
    
def bfs_maze(start,maze,visited,goal):
    move=[start]
    index=[]
    heur=[]
    maze[move[0][0]][move[0][1]]='P'
    while move[0][0]!=goal[0] or move[0][1]!=goal[1]:
        i,j=move[0][0],move[0][1]
        if i>=0 and i<7 and j+1>=0 and j+1<11 and maze[i][j+1]!=0:
            index.append((i,j+1))
            heur.append(maze[i][j+1])
        if i>=0 and i<7 and j-1>=0 and j-1<11 and maze[i][j-1]!=0:
            index.append((i,j-1))
            heur.append(maze[i][j-1])
        if i+1>=0 and i+1<7 and j>=0 and j<11 and maze[i+1][j]!=0:
            index.append((i+1,j))
            heur.append(maze[i+1][j])
        if i-1>=0 and i-1<7 and j>=0 and j<11 and maze[i-1][j]!=0:
            index.append((i-1,j))
            heur.append(maze[i-1][j])
        temp1=np.array(heur)
        temp2=np.array(index)
        sort=np.argsort(temp1)
        heur=list(temp1[sort])
        index=list(temp2[sort])
        move.clear()
        move.append(index[0])
        index.clear()
        heur.clear()
        maze[move[0][0]][move[0][1]]='P'
    for row in maze:
        print(row)
        
def a_star_maze(start,maze,visited,goal):
    queue=PriorityQueue()
    g_score=[[9999 for i in range(11)] for i in range(7)]
    f_score=[[9999 for i in range(11)] for i in range(7)]
    g_score[start[0]][start[1]]=0
    f_score[start[0]][start[1]]=maze[start[0]][start[1]]
    queue.put((f_score[start[0]][start[1]],maze[start[0]][start[1]],(start[0],start[1])))
    while not queue.empty():
        _,_,curr_cell=queue.get()
        maze[curr_cell[0]][curr_cell[1]]='P'
        visited[curr_cell[0]][curr_cell[1]]=True
        
        if curr_cell[0]>=0 and curr_cell[1]+1>=0 and curr_cell[0]<7 and curr_cell[1]+1<11 and maze[curr_cell[0]][curr_cell[1]+1]!=0 and visited[curr_cell[0]][curr_cell[1]+1]==False:
            child_cell=(curr_cell[0],curr_cell[1]+1)
            temp_g_score=g_score[curr_cell[0]][curr_cell[1]]+1
            temp_f_score=temp_g_score+maze[child_cell[0]][child_cell[1]]
            if temp_f_score<f_score[child_cell[0]][child_cell[1]]:
                g_score[child_cell[0]][child_cell[1]]=temp_g_score
                f_score[child_cell[0]][child_cell[1]]=temp_f_score
                queue.put((f_score[child_cell[0]][child_cell[1]],maze[child_cell[0]][child_cell[1]],(child_cell[0],child_cell[1])))
        
        if curr_cell[0]>=0 and curr_cell[1]-1>=0 and curr_cell[0]<7 and curr_cell[1]-1<11 and maze[curr_cell[0]][curr_cell[1]-1]!=0 and visited[curr_cell[0]][curr_cell[1]-1]==False:
            child_cell=(curr_cell[0],curr_cell[1]-1)
            temp_g_score=g_score[curr_cell[0]][curr_cell[1]]+1
            temp_f_score=temp_g_score+maze[child_cell[0]][child_cell[1]]
            if temp_f_score<f_score[child_cell[0]][child_cell[1]]:
                g_score[child_cell[0]][child_cell[1]]=temp_g_score
                f_score[child_cell[0]][child_cell[1]]=temp_f_score
                queue.put((f_score[child_cell[0]][child_cell[1]],maze[child_cell[0]][child_cell[1]],(child_cell[0],child_cell[1])))
        
        if curr_cell[0]+1>=0 and curr_cell[1]>=0 and curr_cell[0]+1<7 and curr_cell[1]<11 and maze[curr_cell[0]+1][curr_cell[1]]!=0 and visited[curr_cell[0]+1][curr_cell[1]]==False:
            child_cell=(curr_cell[0]+1,curr_cell[1])
            temp_g_score=g_score[curr_cell[0]][curr_cell[1]]+1
            temp_f_score=temp_g_score+maze[child_cell[0]][child_cell[1]]
            if temp_f_score<f_score[child_cell[0]][child_cell[1]]:
                g_score[child_cell[0]][child_cell[1]]=temp_g_score
                f_score[child_cell[0]][child_cell[1]]=temp_f_score
                queue.put((f_score[child_cell[0]][child_cell[1]],maze[child_cell[0]][child_cell[1]],(child_cell[0],child_cell[1])))
        
        if curr_cell[0]-1>=0 and curr_cell[1]>=0 and curr_cell[0]-1<7 and curr_cell[1]<11 and maze[curr_cell[0]-1][curr_cell[1]]!=0 and visited[curr_cell[0]-1][curr_cell[1]]==False:
            child_cell=(curr_cell[0]-1,curr_cell[1])
            temp_g_score=g_score[curr_cell[0]][curr_cell[1]]+1
            temp_f_score=temp_g_score+maze[child_cell[0]][child_cell[1]]
            if temp_f_score<f_score[child_cell[0]][child_cell[1]]:
                g_score[child_cell[0]][child_cell[1]]=temp_g_score
                f_score[child_cell[0]][child_cell[1]]=temp_f_score
                queue.put((f_score[child_cell[0]][child_cell[1]],maze[child_cell[0]][child_cell[1]],(child_cell[0],child_cell[1])))
        if curr_cell[0]==goal[0] and curr_cell[1]==goal[1]:
            break
    for row in maze:
        print(row)
maze = [
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1],
    [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [12, 0, 10, 9, 8, 7, 6, 5, 4, 0, 2],
    [13, 0, 11, 0, 0, 0, 0, 0, 5, 0, 3],
    [14, 13, 12, 0, 10, 9, 8, 7, 6, 0, 4],
    [0, 0, 13, 0, 11, 4, 0, 0, 0, 0, 5],
    [16, 15, 14, 0, 12, 11, 10, 9, 8, 7, 6],
]

visited=[[False for i in range(12)] for i in range(7)]

start=(6,0)
goal=(0,10)
print('Greedy BFS Goal: ')
bfs_maze(start,maze,visited,goal)
print()
maze = [
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1],
    [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [12, 0, 10, 9, 8, 7, 6, 5, 4, 0, 2],
    [13, 0, 11, 0, 0, 0, 0, 0, 5, 0, 3],
    [14, 13, 12, 0, 10, 9, 8, 7, 6, 0, 4],
    [0, 0, 13, 0, 11, 4, 0, 0, 0, 0, 5],
    [16, 15, 14, 0, 12, 11, 10, 9, 8, 7, 6],
]

visited=[[False for i in range(12)] for i in range(7)]

start=(6,0)
goal=(0,10)
print('A* Goal: ')
a_star_maze(start,maze,visited,goal)