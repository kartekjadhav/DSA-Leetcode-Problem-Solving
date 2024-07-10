#TC - O(N*N) + O(N), SC - extra space - O(N*2), stack space - O(1)
from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        count = [1 for _ in range(n)]
        maxi = 1
        for ind in range(1, n):
            for prev_ind in range(ind):
                if nums[ind]>nums[prev_ind]:
                    if 1+dp[prev_ind]>dp[ind]:
                        dp[ind] = 1 + dp[prev_ind]
                        #Inherit
                        count[ind] = count[prev_ind]
                    elif 1+dp[prev_ind]==dp[ind]:
                        #Increase the count
                        count[ind] += count[prev_ind]
            maxi = max(maxi, dp[ind])

        ans = 0
        for i in range(n):
            if dp[i]==maxi:
                ans += count[i]
        return ans