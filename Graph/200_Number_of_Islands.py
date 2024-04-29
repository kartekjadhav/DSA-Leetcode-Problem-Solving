#DFS TC-O(N*M*4),SC- stack space - O(N*M), no extra space
#BFS - TC-O(N*M*4), SC - O(N*M)
from typing import List
from queue import Queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            grid[r][c] = '-1'
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for a,b in directions:
                new_r,new_c = r+a,c+b
                if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and grid[new_r][new_c]=='1':
                    dfs(new_r,new_c)
        
        def bfs(r,c):
            q = Queue()
            q.put((r,c))
            grid[r][c] = '-1'
            while not q.empty():
                i,j = q.get()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for a,b in directions:
                    new_r,new_c = i+a,j+b
                    if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and grid[new_r][new_c]=='1':
                        grid[new_r][new_c] = '-1'
                        q.put((new_r,new_c))

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    bfs(i,j)
        return count