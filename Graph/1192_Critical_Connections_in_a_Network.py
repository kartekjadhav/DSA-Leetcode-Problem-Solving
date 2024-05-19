#TC - O(V+2E), SC - O(V+2E)

from typing import List
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(node,parent,timer):
            visited[node] = True
            time[node] = timer
            low[node] = timer
            for i,neighbour in enumerate(adj[node]):
                if parent==neighbour: continue
                if not visited[neighbour]:
                    dfs(neighbour,node,timer+i+1)
                    low[node] = min(low[node],low[neighbour])
                    if low[neighbour]>time[node]:
                        ans.append([node,neighbour])
                else:
                    low[node] = min(low[node],low[neighbour])

        adj = [[] for _ in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        ans = []
        time = [0 for _ in range(n)]
        low = [0 for _ in range(n)]
        visited = [False]*n
        for i in range(n):
            if not visited[i]:
                dfs(i,-1,i)
        return ans