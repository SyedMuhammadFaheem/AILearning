class TSP:
    graph=[]
    visited=[]
    cost={}

    def __init__(self,n):
        self.graph=[[] for i in range(n)]
        self.visited=[False for i in range(n)]
        self.cost=dict()

    def tspInit(self):
        self.graph[0].append(1)
        self.graph[0].append(2)
        self.graph[0].append(3)

        self.graph[1].append(0)
        self.graph[1].append(2)
        self.graph[1].append(3)

        self.graph[2].append(0)
        self.graph[2].append(1)
        self.graph[2].append(3)
        
        self.graph[3].append(0)
        self.graph[3].append(1)
        self.graph[3].append(2)


        self.cost[(0, 1)] = 10
        self.cost[(0, 2)] = 15
        self.cost[(0, 3)] = 20

        self.cost[(1, 0)] = 10
        self.cost[(1, 2)] = 35
        self.cost[(1, 3)] = 25

        self.cost[(2, 0)] = 15
        self.cost[(2, 1)] = 35
        self.cost[(2, 3)] = 30

        self.cost[(3, 0)] = 20
        self.cost[(3, 1)] = 25
        self.cost[(3, 2)] = 30

    def runTSP(self,source):
        
        count=0
        path=[]
        finalCost=0
        tempSource=source
        while [item for item in self.visited if item==True]!=self.visited:
            index=-1
            min=9999
            for i in range(len(self.graph[source])):
                if self.visited[self.graph[source][i]]==False and self.graph[source][i]!=source and min>self.cost[(source,self.graph[source][i])]:
                    min=self.cost[(source,self.graph[source][i])]
                    index=self.graph[source][i]

            if index!=-1:
                finalCost+=self.cost[(source,index)]
                path.append(source)
                self.visited[source]=True
                source=index
                count+=1

            if count==len(self.graph)-1:
                self.visited[tempSource]=False
            elif count==len(self.graph):
                self.visited[tempSource]=True
                path.append(tempSource)

        print(path)
        print(finalCost)


tspObj=TSP(4)
tspObj.tspInit()
tspObj.runTSP(0)
