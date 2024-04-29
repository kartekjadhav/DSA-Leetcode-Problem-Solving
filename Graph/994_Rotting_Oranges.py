#BFS wiil only work here as we would check next level always.
#DFS wont work to get the min time here
#X - N*M
#TC - O(X) + O(X*4) = O(X)
#SC - O(X)
from typing import List
from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = Queue()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.put((i,j))
        time = 0
        while not q.empty():
            size = q.qsize()
            flag = False
            for _ in range(size):
                i,j = q.get()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for a,b in directions:
                    new_r,new_c = i+a,j+b
                    if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and grid[new_r][new_c]==1:
                        flag = True
                        grid[new_r][new_c] = 2
                        q.put((new_r,new_c))
            if flag: time+=1

        #Checking if any fresh oranges left
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1: return -1

        return time