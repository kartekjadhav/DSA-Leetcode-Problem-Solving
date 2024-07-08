from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*(n+1) for _ in range(n+1)]

        for ind in range(n-1, -1, -1):
            for prev_ind in range(ind-1, -2, -1):
                maxi = float('-inf')
                maxi = dp[ind+1][prev_ind+1]
                if prev_ind==-1 or nums[prev_ind]<nums[ind]:
                    maxi = max(maxi, 1 + dp[ind+1][ind+1])
                
                dp[ind][prev_ind+1] = maxi

        return dp[0][0]