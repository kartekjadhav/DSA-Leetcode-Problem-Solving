#TC - O(V+E) , SC - O(V) 

from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indegree = [0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        
        q = deque()
        for i,n in enumerate(indegree):
            if n==0:
                q.append(i)
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)
        return ans