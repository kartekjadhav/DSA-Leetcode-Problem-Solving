#DFS - TC - O(V+2E), SC - stack - O(N), extra - O(N)
#BFS - TC - O(V+2E), SC - extra - O(N)

from typing import List
from queue import Queue

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Code here
        def bfs(src, par):
            q = Queue()
            q.put((src, par))
            visited[src] = 1
            while not q.empty():
                node, parent = q.get()
                for i in adj[node]:
                    if not visited[i]:
                        q.put((i, node))
                        visited[i] = 1
                    elif parent != i:
                        return True
            return False
            
        def dfs(src, parent):
            visited[src] = 1
            for i in adj[src]:
                if not visited[i]:
                    if dfs(i, src):
                        return True
                elif i != parent:
                    return True
            return False
         
        visited = [0] * V
        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        return False
