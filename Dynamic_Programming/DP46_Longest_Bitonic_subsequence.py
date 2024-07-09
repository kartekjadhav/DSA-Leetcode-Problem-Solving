T#TC - O(N*N), SC - extra space - O(N*2), stack space - O(1)
from typing import List
class Solution:
    def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
        # code here
        dp1, dp2 = [1]*n, [1]*n
        
        for ind in range(1, n):
            for prev_ind in range(ind):
                if nums[ind]>nums[prev_ind] and dp1[prev_ind]+1>dp1[ind]:
                    dp1[ind] = 1 + dp1[prev_ind]
        
        
        for ind in range(n-2, -1, -1):
            for prev_ind in range(n-1, ind, -1):
                if nums[ind]>nums[prev_ind] and dp2[prev_ind]+1>dp2[ind]:
                    dp2[ind] = 1 + dp2[prev_ind]
        
        maxi = 0
        for i in range(n):
            if dp1[i]>1 and dp2[i]>1:
                maxi = max(maxi, dp1[i]+dp2[i]-1)
        return maxi