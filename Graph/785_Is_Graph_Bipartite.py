#DFS - TC - O(V) + O(V+2E), SC - extra space - O(V), stack space - O(V)
#BFS - TC - O(V) + O(V+2E), SC - extra space - O(V), stack space - O(1)

from collections import deque
from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        #BFS Solution
        def bfs(node):
            q = deque()
            q.append(node)
            visited[node] = 0
            while q:
                res = q.popleft()
                color = visited[res]
                for neighbour in graph[res]:
                    if visited[neighbour] == color: return False
                    if visited[neighbour] == -1:
                        q.append(neighbour)
                        visited[neighbour] = abs(color-1)
            return True
        
        #DFS Solution
        def dfs(node,color):
            visited[node] = color
            for neighbour in graph[node]:
                if visited[neighbour] == color: return False
                if visited[neighbour] == -1:
                    if not dfs(neighbour,abs(color-1)): 
                        return False
            return True

        n = len(graph)
        visited = [-1]*n

        for i in range(n):
            if visited[i]==-1:
                if not dfs(i,0):
                    return False
        return True
