#TC - O(V)+O(V+E), SC - O(V)
from collections import deque
from typing import List
class Solution:
    def findOrder(self, V: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(V)]
        for val1,val2 in prerequisites:
            adj[val2].append(val1)
        
        indegree = [0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1

        q = deque()
        for i,val in enumerate(indegree):
            if not val:
                q.append(i)
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if not indegree[neighbour]:
                    q.append(neighbour)
        return ans if V==len(ans) else []