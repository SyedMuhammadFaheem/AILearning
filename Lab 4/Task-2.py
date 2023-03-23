#Task 2
import networkx as nx
import matplotlib.pyplot as plt
def dfs(graph,source,goal_vertex):
    global path
    global goal_check
    for i in range(len(graph[source])):
        if graph[source][i]==goal_vertex:
            path.append((source,graph[source][i]))
            goal_check=True
        if goal_check:
            break
        path.append((source,graph[source][i]))
        dfs(graph,graph[source][i],goal_vertex)
    if goal_check and source==0:
        return path
       
def dfs_graph(graph,source,goal_vertex,visited):
    global path
    global goal_check
    visited[source]=True
    for i in range(len(graph[source])):
        if graph[source][i]==goal_vertex:
            path.append((source,graph[source][i]))
            goal_check=True
        if goal_check:
            break
        if visited[graph[source][i]]==False:
            path.append((source,graph[source][i]))
            visited[graph[source][i]]=True
            dfs_graph(graph,graph[source][i],goal_vertex,visited)
    if goal_check and source==0:
        return path 


def dfs_init():
    graph=[[] for i in range(11)]
    graph[0].append(1)
    graph[0].append(2)
    graph[1].append(3)
    graph[1].append(4)
    graph[2].append(5)
    graph[2].append(6)
    graph[3].append(7)
    graph[3].append(8)
    graph[4].append(9)
    graph[5].append(10)
    return graph

def dfs_init_graph():
    visited=[False for i in range(6)]
    graph=[[] for i in range(6)]
    graph[0].append(1)
    graph[0].append(2)
    graph[0].append(3)
    graph[1].append(0)
    graph[1].append(3)
    graph[2].append(0)
    graph[2].append(3)
    graph[2].append(4)
    graph[3].append(0)
    graph[3].append(1)
    graph[3].append(2)
    graph[3].append(4)
    graph[4].append(2)
    graph[4].append(3)
    graph[4].append(5)
    graph[5].append(4)
    return graph,visited

def genGraph(path,count):
    print(path)
    G=nx.DiGraph()
    G.add_nodes_from([item for item in range(count)])
    G.add_edges_from(path)
    nx.draw(G,with_labels=True)
    plt.show()

print("DFS on a tree")
path=[]
goal_check=False
graph=dfs_init() 
res_path=dfs(graph,0,9)
genGraph(res_path,11)

print("DFS on a graph")
path=[]
goal_check=False
graph,visited=dfs_init_graph()
res_path=dfs_graph(graph,0,5,visited)
genGraph(res_path,6)