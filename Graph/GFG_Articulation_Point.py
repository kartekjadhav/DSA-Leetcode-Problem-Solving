#TC - O(V+2E), SC - O(N)

import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def __init__(self):
        self.timer = 0
        
    def articulationPoints(self, V, adj):
        # code here
        def dfs(node,parent):
            visited[node] = True
            time[node],low[node] = self.timer,self.timer
            self.timer+=1
            child = 0
            for neighbour in adj[node]:
                if neighbour==parent: continue
                if not visited[neighbour]:
                    dfs(neighbour,node)
                    low[node] = min(low[node],low[neighbour])
                    if low[neighbour]>=time[node] and parent!=-1:
                        isArtiPoint[node] = True
                    child+=1
                else:
                    low[node] = min(low[node],time[neighbour])
            if parent==-1 and child>1:
                isArtiPoint[node] = True
        
        visited = [False]*V
        isArtiPoint = [False]*V
        time = [0]*V
        low = [0]*V
        
        for node in range(V):
            if not visited[node]:
                dfs(node,-1)
        ans = []
        for i,n in enumerate(isArtiPoint):
            if n: ans.append(i)
        return ans if ans else [-1]