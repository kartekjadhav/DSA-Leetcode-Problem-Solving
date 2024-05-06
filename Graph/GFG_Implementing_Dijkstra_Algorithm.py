#TC - O(E*logV)

#Using Priority Queue

import heapq
class Solution:
    def dijkstra(self, V, adj, S):
        #code here
        distance = [float("inf")]*V
        distance[S] = 0
        hp = [(0,S)]
        
        while hp:
            dist,node = heapq.heappop(hp)
            for neighbour,weight in adj[node]:
                if dist+weight < distance[neighbour]:
                    distance[neighbour] = dist+weight
                    heapq.heappush(hp,(dist+weight,neighbour))
        return distance
    
#Using SortedSet

from sortedcontainers import SortedSet
class Solution:
    def dijkstra(self, V, adj, S):
        #code here
        distance = [float("inf")]*V
        distance[S] = 0
        sorted_set = SortedSet()
        sorted_set.add((0,S))
        
        while sorted_set:
            dist,node = sorted_set[0]
            sorted_set.remove((dist,node))
            for neighbour,weight in adj[node]:
                if dist+weight < distance[neighbour]:
                    if distance[neighbour]!=float("inf"):
                        sorted_set.remove((distance[neighbour],neighbour))
                    distance[neighbour] = dist+weight
                    sorted_set.add((dist+weight,neighbour))
                        
        return distance