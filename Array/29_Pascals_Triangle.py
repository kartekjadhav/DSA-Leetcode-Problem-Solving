#TC - O(N^2), SC - O(N^2)
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(ans[-1][j-1] + ans[-1][j])
            temp.append(1)
            ans.append(temp)
        return ans