#This is followup question of DP14, so i have directly taken tabulation space optimized solution here

#TC - O(N + N*K), SC - O(K)
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def findSum(k):
            prev = [False for _ in range(k+1)]
            prev[0] = True
            if nums[0]<=k: prev[nums[0]] = True
            
            for ind in range(1, len(nums)):
                curr = [False for _ in range(k+1)]
                curr[0] = True
                for target in range(1, k+1):
                    notpick = prev[target]
                    pick = False
                    if target>=nums[ind]: pick = prev[target-nums[ind]]
                    curr[target] = pick or notpick
                prev = curr
            return prev[k]
        
        total = sum(nums)
        if total%2: return False
        return findSum(total//2)