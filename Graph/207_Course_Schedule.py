#TC - O(V+E), SC - O(V)
from collections import deque
from typing import List
class Solution:
    def canFinish(self, V: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(V)]
        for i,j in prerequisites:
            adj[j].append(i)
        
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
        
        return V==count