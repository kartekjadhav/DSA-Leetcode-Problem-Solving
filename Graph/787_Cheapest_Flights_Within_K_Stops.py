#TC - E, SC - O(E*V)
from collections import deque
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q = deque()
        #   stops,cost,src_city
        q.append((0,0,src))
        adj = [[] for _ in range(n)]
        for start,end,cost in flights:
            adj[start].append((end,cost))
        cost = [float("inf") for _ in range(n)]
        cost[src] = 0
        while q:
            curr_stops,curr_cost,curr_city = q.popleft()
            if curr_stops>k: continue
            for neighbour,price in adj[curr_city]:
                if curr_stops<=k and cost[neighbour]>curr_cost+price:
                    cost[neighbour] = curr_cost+price
                    q.append((curr_stops+1,price+curr_cost,neighbour))
        if cost[dst]!=float("inf"):
            return cost[dst]
        else: return -1