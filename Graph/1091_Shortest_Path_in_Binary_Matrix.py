#TC - O(8*N^2), SC - O(N^2)

from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n==1:
            if grid[0][0]==0: return 1
            else: return -1
        
        distance = [[float("inf")]*n for _ in range(n)]
        q = deque()
        if grid[0][0]==0: 
            q.append((1,0,0))
            distance[0][0] = 1
        delta = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        while q:
            dist,r,c = q.popleft()
            for a,b in delta:
                new_r,new_c = r+a,c+b
                if 0<=new_r<n and 0<=new_c<n and (not grid[new_r][new_c]) and dist+1<distance[new_r][new_c]:
                    if new_r==n-1 and new_c==n-1: return dist+1
                    distance[new_r][new_c] = dist+1
                    q.append((dist+1,new_r,new_c))
        return -1