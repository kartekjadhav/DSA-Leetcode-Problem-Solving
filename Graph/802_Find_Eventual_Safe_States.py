#TC - O(V) + O(V+E), SC - stack - O(V), extra - O(V)
from typing import List
from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            visited[node] = True
            path[node] = True
            flag = True
            for neighbour in graph[node]:
                if not safeNode[neighbour] or (visited[neighbour] and path[neighbour]):
                    flag = False
                    break
                elif not visited[neighbour]:
                    if not dfs(neighbour):
                        flag = False
                        break
            path[node] = False
            safeNode[node] = flag
            return flag

        n = len(graph)
        path = [False]*n
        visited = [False]*n
        safeNode = [True]*n
        ans = []
        for i in range(n):
            if not visited[i]:
                dfs(i)
        for i,value in enumerate(safeNode):
            if value: ans.append(i)
        return ans
    
#Using Kahn's Algo
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in graph[i]:
                adj[j].append(i)
        indegree = [0]*n
        for i in range(n):
            for j in adj[i]:
                indegree[j]+=1
        q = deque()
        for i,n in enumerate(indegree):
            if not n:
                q.append(i)
        
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if not indegree[neighbour]:
                    q.append(neighbour)
        
        ans.sort()
        return ans