#TC - O(V) + O(V+E), SC - stack - O(V), extra - O(V)
from typing import List
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