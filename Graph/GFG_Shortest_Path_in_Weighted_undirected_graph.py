import heapq
from typing import List
class Solution:
    def shortestPath(self,n,m,edges)->List[int]:
        # code here
        adj = [[] for _ in range(n+1)]
        for start,end,weight in edges:
            adj[start].append((end,weight))
            adj[end].append((start,weight))
        
        hp = [(0,[1])]
        distance = [float("inf")]*(n+1)
        distance[1] = 0
        while hp:
            dist,temp_list = heapq.heappop(hp)
            node = temp_list[-1]
            
            if node==n:
                return [dist] + temp_list
                
            for neighbour,weight in adj[node]:
                if dist+weight<distance[neighbour]:
                    distance[neighbour] = dist+weight
                    heapq.heappush(hp,(dist+weight,temp_list+[neighbour]))

        return [-1]
    
#Striver solution using parent array(from where it came)
#TC - O(ElogV) + O(V)
#SC - O(N+M)

import heapq
from typing import List
class Solution:
    def shortestPath(self,n,m,edges)->List[int]:
        # code here
        adj = [[] for _ in range(n+1)]
        for start,end,weight in edges:
            adj[start].append((end,weight))
            adj[end].append((start,weight))
        
        hp = [(0,1)]
        distance = [float("inf")]*(n+1)
        distance[1] = 0
        parent = [i for i in range(n+1)]
        parent[1] = 1
        parent[0] = -1
        while hp:
            dist,node = heapq.heappop(hp)
                
            for neighbour,weight in adj[node]:
                if dist+weight<distance[neighbour]:
                    distance[neighbour] = dist+weight
                    parent[neighbour] = node
                    heapq.heappush(hp,(dist+weight,neighbour))
        
        ans = []
        node = n
        # O(N)
        while node!=parent[node]:
            ans.append(node)
            node = parent[node]
        
        if ans:
            ans.append(1)
            ans.append(distance[n])

        return list(reversed(ans)) if ans else [-1]