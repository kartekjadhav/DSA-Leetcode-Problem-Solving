#Note - Use DisjointSet template from DisjointSet.py file in this list
#TC - O(N^2 * 4),SC - O(N^2)
from typing import List
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsj = DisjointSet(n*n) # type: ignore
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(n):
            for c in range(n):
                if not grid[r][c]: continue
                position = r*n + c
                for delr,delc in directions:
                    adjr,adjc = r+delr,c+delc
                    adjPosition = adjr*n + adjc
                    if 0<=adjr<n and 0<=adjc<n and grid[adjr][adjc]:
                        if dsj.findPar(position)!=dsj.findPar(adjPosition):
                            dsj.unionSize(position,dsj.findPar(adjPosition))

        result = max(dsj.size)
        for r in range(n):
            for c in range(n):
                if grid[r][c]==0:
                    count = 1
                    currPar = r*n + c
                    parSet = {currPar}
                    for delr,delc in directions:
                        adjr,adjc = r+delr,c+delc
                        adjPosition = adjr*n + adjc
                        if 0<=adjr<n and 0<=adjc<n and grid[adjr][adjc] and dsj.findPar(adjPosition) not in parSet:
                            parSet.add(dsj.findPar(adjPosition))
                            count+=dsj.size[dsj.findPar(adjPosition)]
                    result = max(result,count)
        return result