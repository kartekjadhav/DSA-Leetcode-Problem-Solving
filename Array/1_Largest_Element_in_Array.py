from typing import List
class Solution:
    def largest(self, n : int, arr : List[int]) -> int:
        # code here
        maxi = arr[0]
        for i in range(1,n):
            maxi = max(maxi, arr[i])
        return maxi