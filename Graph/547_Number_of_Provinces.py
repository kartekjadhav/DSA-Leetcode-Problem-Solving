#DFS - TC - O(N)(OUTER LOOP) + O(V+2E)(FOR DFS), SC - extra - O(V), stack space - O(V)
#BFS - TC - O(N)(OUTER LOOP) + O(V+2E)(FOR BFS), SC - extra - O(V)
from queue import Queue
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        #Breadth First Search
        def bfs(node):
            q = Queue()
            q.put(node)
            visit[node] = 1
            while not q.empty():
                res = q.get()
                for i in adjList[res]:
                    if not visit[i]:
                        q.put(i)
                        visit[i] = 1
        
        #Depth First Search
        def dfs(node):
            visit[node] = 1
            for i in adjList[node]:
                if not visit[i]:
                    dfs(i)
        
        #Convert Adj matrix to Adj list
        n = len(isConnected)
        adjList = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adjList[i].append(j)
                    adjList[j].append(i)
        
        count = 0
        visit = [0]*n
        for i in range(n):
            if not visit[i]:
                count+=1
                bfs(i)
        return count
    

#Using Disjoint Set (Take Disjoint Set template from Disjoint_Set.py in this list)
#TC - O(N^2), SC - O(N)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsj = DisjointSet(n)  # type:ignore
        #O(N^2)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    dsj.unionSize(i,j)
        count = 0
        #O(N)
        for i in range(n):
            if dsj.findPar(i)==i: count+=1
        return count