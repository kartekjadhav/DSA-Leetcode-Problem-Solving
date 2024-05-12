from typing import List
import heapq

#Using Floyd Warshall Algo
#TC - O(N^3), SC - O(N^2)
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[float('inf')]*n for _ in range(n)]
        for u,v,wt in edges:
            matrix[u][v] = wt
            matrix[v][u] = wt
        
        for i in range(n):
            matrix[i][i] = 0

        for tr in range(n):
            for i in range(n):
                for j in range(n):
                    if i == tr or j == tr or i == j:
                        continue
                    matrix[i][j] = min(matrix[i][j], matrix[i][tr] + matrix[tr][j])

        ans,mini = 0,float('inf')
        for i in range(n):
            count = 0
            for j in range(n):
                if i==j: continue
                if matrix[i][j]<=distanceThreshold:
                    count+=1
                    if count>mini: break
            if count<=mini:
                mini = count
                ans = i
        return ans

#Using Dijkstra's Algo
#TC - O(N*E*logV), SC - O(N^2)
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def dijkstra(start):
            distance = [float("inf")]*n
            distance[start] = 0
            hp = [(0,start)]
            
            while hp:
                dist,city = heapq.heappop(hp)
                for neighbour,wt in adj[city]:
                    if dist+wt < distance[neighbour]:
                        distance[neighbour] = dist+wt
                        heapq.heappush(hp,(dist+wt,neighbour))
            return distance

        #Creating Adj List
        matrix = [[] for _ in range(n)]
        adj = [[] for _ in range(n)]

        #Filling Adj List
        for u,v,wt in edges:
            adj[u].append((v,wt))
            adj[v].append((u,wt))
        
        for i in range(n):
            matrix[i] = dijkstra(i)
        
        #Finding answer
        ans,mini = 0,float('inf')
        for i in range(n):
            count = 0
            for j in range(n):
                if i==j: continue
                if matrix[i][j]<=distanceThreshold:
                    count+=1
                    if count>mini: break
            if count<=mini:
                mini = count
                ans = i
        return ans