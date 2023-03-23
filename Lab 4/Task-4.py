#Task 4
import networkx as nx
import matplotlib.pyplot as plt
def dfs_graph(graph,source,goal_vertex,visited):
    global goal_check
    global path
    global source_store
    if path==[]:
        source_store=source
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
    if goal_check and source==source_store:
        return path

def bi_directional_search(source,goal,middle_node,graph,visited):
    path1=dfs_graph(graph,source,middle_node,visited)
    graph,visited=dfs_init_graph()
    path2=dfs_graph(graph,goal,middle_node,visited)
    if path1[-1][1]==path2[-1][1]:
        print('Goal State found!')
        final_path2=[]
        path2.reverse()
        for i in range(len(path2)):
            final_path2.append((path2[i][1],path2[i][0]))
        return path1+final_path2
    else:
        print('Goal State not found!')
        return []
    
    
def dfs_init_graph():
    global goal_check
    global path
    goal_check=False
    path=[]
    visited=[False for i in range(16)]
    graph=[[] for i in range(16)]
    graph[0].append(3)
    graph[1].append(3)
    graph[2].append(5)
    graph[3].append(0)
    graph[3].append(7)
    graph[3].append(1)
    graph[4].append(5)
    graph[5].append(2)
    graph[5].append(4)
    graph[5].append(7)
    graph[7].append(8)
    graph[7].append(3)
    graph[7].append(5)
    graph[8].append(7)
    graph[8].append(9)
    graph[9].append(8)
    graph[9].append(10)
    graph[9].append(11)
    graph[10].append(9)
    graph[10].append(12)
    graph[10].append(13)
    graph[11].append(9)
    graph[11].append(14)
    graph[11].append(15)
    graph[12].append(10)
    graph[13].append(10)
    graph[14].append(11)
    graph[15].append(11)
    return graph,visited


def genGraph(path,count):
    print(path)
    G=nx.DiGraph()
    G.add_nodes_from([item for item in range(count)])
    G.add_edges_from(path)
    nx.draw(G,with_labels=True)
    plt.show()
path=[]
source_store=0
graph,visited=dfs_init_graph()
res_path=bi_directional_search(0,15,8,graph,visited)
genGraph(res_path,16)