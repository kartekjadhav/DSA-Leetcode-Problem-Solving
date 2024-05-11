#TC - ElogV = m*n*4log(m*n)
#SC - O(m*n)

from typing import List
import heapq
class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        distance = [[float("inf")]*n for _ in range(m)]
        distance[0][0] = 0
        hp = [(0,0,0)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while hp:
            effort,r,c = heapq.heappop(hp)
            if (r,c) == (m-1,n-1): 
                return effort
            for a,b in directions:
                new_r,new_c = r+a,c+b
                if 0<=new_r<m and 0<=new_c<n:
                    newEffort = max(effort,abs(grid[new_r][new_c]-grid[r][c]))
                    if newEffort<distance[new_r][new_c]:
                        distance[new_r][new_c] = newEffort
                        heapq.heappush(hp,(newEffort,new_r,new_c))
        
        return 0