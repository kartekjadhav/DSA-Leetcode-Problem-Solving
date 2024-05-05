from collections import deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
    
        def dfs_topo(node):
            visited[node] = True
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    dfs_topo(neighbour)
            stack.append(node)
        
        adj = [[] for _ in range(K)]
        for i in range(N-1):
            s1,s2 = alien_dict[i],alien_dict[i+1]
            for j in range(min(len(s1),len(s2))):
                if s1[j]!=s2[j]:
                    adj[ord(s1[j])-97].append(ord(s2[j])-97)
                    break
        
        ans = []
        visited = [False]*K
        stack = []
        for i in range(K):
            if not visited[i]:
                dfs_topo(i)
        while stack:
            ans.append(chr(97+stack.pop()))
        return "".join(ans)
    
#Using Kahn's algo
from collections import deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        adj = [[] for _ in range(K)]
        for i in range(N-1):
            s1,s2 = alien_dict[i],alien_dict[i+1]
            for j in range(min(len(s1),len(s2))):
                if s1[j]!=s2[j]:
                    adj[ord(s1[j])-97].append(ord(s2[j])-97)
                    break
        
        indegree = [0]*K
        for i in range(K):
            for j in adj[i]:
                indegree[j]+=1
            
        ans = []
        q= deque()
        
        for i in range(K):
            if not indegree[i]: 
                q.append(i)
        visited = [False]*K
        
        while q:
            node = q.popleft()
            ans.append(chr(97+node))
            visited[node] = True
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if not indegree[neighbour]:
                    q.append(neighbour)
        
        for i,n in enumerate(visited):
            if not n: ans.append(chr(97+i))
        
        return "".join(ans)