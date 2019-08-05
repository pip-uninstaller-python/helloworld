'''
对一个有向无环图G进行拓扑排序，是将G中所有顶点排成一个线性序列，
使得图中任意一对顶点u和v，若边(u,v)∈E(G)，则u在线性序列中出现在v之前。
通常，这样的线性序列称为满足拓扑次序(Topological Order)的序列，简称拓扑序列。
简单的说，由某个集合上的一个偏序得到该集合上的一个全序，这个操作称之为拓扑排序。
每个顶点出现且只出现一次；
若A在序列中排在B的前面，则在图中不存在从B到A的路径。
'''
from collections import defaultdict 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def topologicalSortUtil(self,v,visited,stack): 
        visited[v] = True
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
        stack.insert(0,v) 
    def topologicalSort(self): 
        visited = [False]*self.V 
        stack =[] 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
        print (stack) 
g= Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
print ("拓扑排序结果：")
g.topologicalSort()
