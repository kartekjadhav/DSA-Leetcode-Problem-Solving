#TC - O(N*N) + O(N), SC - extra space - O(N), stack space - O(1)
from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1]*n
        lastindex = 0
        maxi = float('-inf')
        lastind = [i for i in range(n)]
        for ind in range(1,n):
            for prev in range(ind):
                if nums[ind]%nums[prev]==0 and 1+dp[prev]>dp[ind]:
                    dp[ind] = 1 + dp[prev]
                    lastind[ind] = prev
                if maxi<dp[ind]:
                    maxi = dp[ind]
                    lastindex = ind
                    
        
        ans = []
        while lastindex!=lastind[lastindex]:
            ans.append(nums[lastindex])
            lastindex = lastind[lastindex]
        ans.append(nums[lastindex])
        return reversed(ans)