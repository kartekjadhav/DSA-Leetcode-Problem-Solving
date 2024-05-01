#DFS -> TC - O(N*M*4), SC - O(1), stack space - O(N*M)
#BFS -> TC - O(N*M*4), SC - O(1)

from collections import deque
from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            while q:
                i,j = q.popleft()
                for a,b in directions:
                    new_r,new_c = i+a,j+b
                    if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and grid[new_r][new_c]==1:
                        q.append((new_r,new_c))
                        grid[new_r][new_c] = 0 

        def dfs(r,c):
            grid[r][c] = 0
            for a,b in directions:
                new_r,new_c = r+a,c+b
                if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and grid[new_r][new_c]==1:
                    dfs(new_r,new_c)

        m,n = len(grid),len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        #Trversing Top and Bottom row
        for j in range(n):
            #Checking Top row
            if grid[0][j]==1:
                bfs(0,j)
            #Checking Bottom row
            if grid[m-1][j]==1:
                bfs(m-1,j)
        
        #Trversing First and Last col
        for i in range(m):
            #Checking Top row
            if grid[i][0]==1:
                bfs(i,0)
            #Checking Bottom row
            if grid[i][n-1]==1:
                bfs(i,n-1)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1: count+=1
        return count
        

        
