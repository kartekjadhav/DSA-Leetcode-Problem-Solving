#DFS - TC - O(N*M) + O(N*M*4), SC - extra - O(N*M), stack space - O(N*M) 
#BFS - TC - O(N*M) + O(N*M*4), SC - extra - O(N*M), stack space - O(1)

import sys
from collections import deque
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        #BFS SOLUTION
        def bfs(r,c,base_r,base_c):
            q = deque()
            q.append((r,c))
            visited[r][c] = True
            ds.append((r-base_r,c-base_c))
            while q:
                i,j = q.popleft()
                for a,b in directions:
                    new_r,new_c = i+a,j+b
                    if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and grid[new_r][new_c]==1 and (not visited[new_r][new_c]):
                        q.append((new_r,new_c))
                        visited[new_r][new_c] = True
                        ds.append((new_r-base_r,new_c-base_c))
                    
        #DFS SOLUTION
        def dfs(r,c,base_r,base_c):
            visited[r][c] = True
            ds.append((r-base_r,c-base_c))
            for a,b in directions:
                new_r,new_c = r+a,c+b
                if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and grid[new_r][new_c]==1 and (not visited[new_r][new_c]):
                    dfs(new_r,new_c,base_r,base_c)
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]    
        shapeset = set()
        m,n = len(grid),len(grid[0])
        visited = [[False]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (not visited[i][j]):
                    ds = []
                    bfs(i,j,i,j)
                    shapeset.add(tuple(ds))
        return len(shapeset)
