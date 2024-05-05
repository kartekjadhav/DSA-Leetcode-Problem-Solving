#Using DFS

from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        def dfs_topo(node,dist):
            for end,weight in adj[node]:
                if distance[end]==-1 or dist+weight < distance[end]:
                    distance[end] = dist+weight
                    dfs_topo(end,dist+weight)
        
        adj = [[] for _ in range(n)]
        for start,end,weight in edges:
            adj[start].append((end,weight))
        
        distance = [-1]*n
        distance[0] = 0
        dfs_topo(0,0)
        return distance
    
#Using BFS

from typing import List
from collections import deque
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(n)]
        for start,end,weight in edges:
            adj[start].append((end,weight))
        
        distance = [-1]*n
        distance[0] = 0
        
        q = deque()
        q.append((0,0))
        
        while q:
            node,dist = q.popleft()
            for neighbour,weight in adj[node]:
                if distance[neighbour]==-1 or dist+weight < distance[neighbour]:
                    distance[neighbour] = dist+weight
                    q.append((neighbour,dist+weight))
            
        return distance