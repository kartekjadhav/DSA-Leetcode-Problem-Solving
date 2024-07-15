#TC - O(m*n), SC - extra space - O(m*n), stack space - O(1)
from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        temp = [[0]*n for _ in range(m)]
        totalSquares = 0

        for i in range(1,m):
            if matrix[i][0] == 1:
                temp[i][0] = 1
                totalSquares += 1
        for j in range(n):
            if matrix[0][j] == 1:
                temp[0][j] = 1
                totalSquares += 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    temp[i][j] = 1 + min(temp[i-1][j], temp[i][j-1], temp[i-1][j-1])
                    totalSquares += temp[i][j]
        return totalSquares