from typing import List
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m,n = len(rowSum), len(colSum)
        temp_rowSum, temp_colSum = rowSum[:], colSum[:]
        ans = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                res = min(temp_rowSum[i], temp_colSum[j])
                ans[i][j] = res
                temp_rowSum[i] -= res
                temp_colSum[j] -= res
        return ans