def alphaBetaPruning(source,depth,maximizing,alpha,beta):
    global graph
    if graph[source][0][1]==-1 and depth<15:
        return graph[source][0][0]

    if maximizing:
        bestVal=-999
        for node in graph[source]:
            value=alphaBetaPruning(node[1],depth+1,not maximizing,alpha,beta)
            bestVal=max(bestVal,value)
            alpha=max(alpha,bestVal)
            if beta<=alpha:
                break
        return bestVal
    else:
        bestVal=999
        for node in graph[source]:
            value=alphaBetaPruning(node[1],depth+1,not maximizing,alpha,beta)
            bestVal=min(bestVal,value)
            alpha=min(alpha,bestVal)
            if beta<=alpha:
                break
        return bestVal


def treeInit():
    graph=[[] for i in range(15)]
    graph[0].append((0,1))
    graph[0].append((0,2))
    graph[1].append((0,3))
    graph[1].append((0,4))
    graph[2].append((0,5))
    graph[2].append((0,6))
    graph[3].append((0,7))
    graph[3].append((0,8))
    graph[4].append((0,9))
    graph[4].append((0,10))
    graph[5].append((0,11))
    graph[5].append((0,12))
    graph[6].append((0,13))
    graph[6].append((0,14))
    graph[7].append((2,-1))
    graph[8].append((4,-1))
    graph[9].append((6,-1))
    graph[10].append((8,-1))
    graph[11].append((1,-1))
    graph[12].append((2,-1))
    graph[13].append((10,-1))
    graph[14].append((12,-1))
    return graph

graph=treeInit()
print("The resultant value is:",alphaBetaPruning(0,0,True,-999,999))
