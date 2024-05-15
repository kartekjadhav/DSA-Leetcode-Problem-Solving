#Note - Use DisjointSet template from DisjointSet.py file in this list
#On Leetcode this questions is  named Number Of Islands II
#TC - O(a*b*4), SC - O(M*N)
#a - len(operator), b - max of len(operator[i])
from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # code here
        m,n = rows,cols
        visited = [[False]*n for _ in range(m)]
        dsj = DisjointSet(m*n) # type: ignore
        result = []
        count = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i,j in operators:
            if not visited[i][j]:
                visited[i][j] = True
                count += 1
                position = i*n + j
                for delr,delc in directions:
                    new_r,new_c = i+delr, j+delc
                    del_position = new_r*n + new_c
                    if 0<=new_r<m and 0<=new_c<n and visited[new_r][new_c] and dsj.findPar(position)!=dsj.findPar(del_position):
                        dsj.unionSize(position,del_position)
                        count-=1
            result.append(count)
        return result