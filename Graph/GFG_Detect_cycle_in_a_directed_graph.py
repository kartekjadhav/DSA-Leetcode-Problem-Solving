#DFS - TC = O(N)(LOOP IN MAIN) + O(V+2E) (FOR DFS), SC - extra - O(N), stack space - O(N) 

from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        def dfs(node):
            if visited[node] and path[node]: return True
            if visited[node] and (not path[node]): return False
            visited[node] = 1
            path[node] = 1
            for neighbour in adj[node]:
                if dfs(neighbour): return True
            path[node] = 0
            return False
        
        visited = [0]*V
        path = [0]*V
        for i in range(V):
            if not visited[i]:
                if dfs(i): return True
        
        return False
    
#Using Kahn's Algorithm
from collections import deque
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        indegree = [0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        
        q = deque()
        for i,n in enumerate(indegree):
            if not n: q.append(i)
        
        count = 0
        
        while q:
            node = q.popleft()
            count+=1
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if not indegree[neighbour]:
                    q.append(neighbour)
        
        return not count==V
        