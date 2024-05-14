import heapq


#1. Prim's Algo
class Solution:
    
    #To return value of Minimum Spanning Tree
    def spanningTree(self, V, adj_list):
        #code here
        visited = [False]*V
        #Wt and Node
        hp = [(0,0)]
        total = 0
        while hp:
            wt,node = heapq.heappop(hp)
            if visited[node]: continue
            total+=wt
            visited[node] = True
            for neighbour,weight in adj_list[node]:
                if not visited[neighbour]:
                    heapq.heappush(hp,(weight,neighbour))
        return total

    #To return the edges of Minimum Spanning Tree
    def spanningTree(self, V, adj_list):
        #code here
        V = 5
        adj_list = [[(1,2),(3,6)],[(0,2),(2,3),(4,5),(3,8)],[(1,3),(4,7)],[(0,6),(1,8)],[(1,5),(2,7)]]
        visited = [False]*V
        #Wt,Node,Parent
        hp = [(0,0,-1)]
        total = 0
        MST = []
        while hp:
            wt,node,parent = heapq.heappop(hp)
            if visited[node]: continue
            if parent!=-1:
                MST.append((parent,node))
            total+=wt
            visited[node] = True
            for neighbour,weight in adj_list[node]:
                if not visited[neighbour]:
                    heapq.heappush(hp,(weight,neighbour,node))
        print(total,MST)
        
        
#2. Kruskal's Algo
class Solution:
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        adj_list = []
        for i in range(V):
            for neighbour,wt in adj[i]:
                adj_list.append((wt,i,neighbour))
        
        adj_list.sort()
        dsj = DisjointSet(V)
        mstWt = 0
        for wt,u,v in adj_list:
            if dsj.findPar(u)!=dsj.findPar(v):
                mstWt += wt
                dsj.unionSize(u,v)
        return mstWt 