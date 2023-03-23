#Task 1
import networkx as nx
import matplotlib.pyplot as plt
def tsp(source,graph,cost,visited):
    nodes_count=4
    path=[]
    final_cost=0
    i=source
    count=0
    while list((item for item in visited if item==True))!=visited:
        minimum=9999
        ver=-1
        for j in range(len(graph[i])):
            if visited[graph[i][j]]==False and graph[i][j]!=i and minimum>cost[(i,graph[i][j])]:
                minimum=cost[(i,graph[i][j])]
                ver=graph[i][j]
        if ver!=-1:
            count+=1
            path.append((i,ver,minimum))
            final_cost+=cost[(i,ver)]
            visited[i]=True
            i=ver
        if count==nodes_count-1:
            visited[source]=False
        elif count==nodes_count:
            visited[source]=True
    print('Final Cost: ',final_cost)
    return path

    
def tsp_init():
    visited=[False,False,False,False]
    graph,cost = [[] for i in range(4)],{}
    graph[0].append(1)
    graph[0].append(2)
    graph[0].append(3)

    graph[1].append(0)
    graph[1].append(2)
    graph[1].append(3)

    graph[2].append(0)
    graph[2].append(1)
    graph[2].append(3)
    
    graph[3].append(0)
    graph[3].append(1)
    graph[3].append(2)


    cost[(0, 1)] = 10
    cost[(0, 2)] = 15
    cost[(0, 3)] = 20

    cost[(1, 0)] = 10
    cost[(1, 2)] = 35
    cost[(1, 3)] = 25

    cost[(2, 0)] = 15
    cost[(2, 1)] = 35
    cost[(2, 3)] = 30

    cost[(3, 0)] = 20
    cost[(3, 1)] = 25
    cost[(3, 2)] = 30
    
    return graph,cost,visited


def genGraph(path):
    print(path)
    G=nx.DiGraph()
    G.add_nodes_from([0,1,2,3])
    G.add_weighted_edges_from(path)
    pos={0:[3,3],1:[1,1],2:[5,1],3:[3,2]}
    weight=nx.get_edge_attributes(G,'weight')
    nx.draw(G,pos=pos,with_labels=True)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=weight)
    plt.show()
    
#source 0
print('Source: ',0)
graph,cost,visited=tsp_init()
path=tsp(0,graph,cost,visited)
genGraph(path)
#source 1
print('Source: ',1)
graph,cost,visited=tsp_init()
path=tsp(1,graph,cost,visited)
genGraph(path)
#source 2
print('Source: ',2)
graph,cost,visited=tsp_init()
path=tsp(2,graph,cost,visited)
genGraph(path)
#source 3
print('Source: ',3)
graph,cost,visited=tsp_init()
path=tsp(3,graph,cost,visited)
genGraph(path)