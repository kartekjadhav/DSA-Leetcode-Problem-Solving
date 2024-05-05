#Using simple BFS

from collections import deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        
        adj = [[] for _ in range(n)]
        for node,neighbour in edges:
            adj[node].append(neighbour)
            adj[neighbour].append(node)
        
        distance = [-1]*n
        distance[src] = 0
        
        q = deque()
        q.append((src,0))
        
        while q:
            node,dist = q.popleft()
            for neighbour in adj[node]:
                if distance[neighbour]==-1 or distance[neighbour] > dist+1:
                    distance[neighbour] = dist+1
                    q.append((neighbour,dist+1))
        
        return distance