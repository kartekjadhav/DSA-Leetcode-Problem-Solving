from typing import List

#Memorization
#TC - O(2^N), SC - O(N)(FOR DP ARRAY) + O(N)(STACK SPACE)
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(index):
            if index==0: return nums[0]
            if index<0: return 0
            if dp[index]!=-1: return dp[index]
            pick = nums[index] + helper(index-2)
            notpick = 0 + helper(index-1)
            dp[index] = max(pick,notpick) 
            return dp[index]
        
        n = len(nums)
        dp = [-1]*n
        return helper(n-1)

#Tabulation
#TC - O(N), SC - O(N)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        dp [0] = nums[0]
        for i in range(1,n):
            pick = float("-inf")
            if i>1:
                pick = nums[i] + dp[i-2]
            else:
                pick = nums[i] + 0
            notpick = 0 + dp[i-1]
            dp[i] = max(pick,notpick)
        return dp[n-1]

#Tabulation with space optimization
#TC - O(N), SC - O(1)
#TABULATION
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2,prev1 = 0,nums[0]
        for i in range(1,n):
            pick = nums[i]
            if i>1:
                pick += prev2
            notpick = 0 + prev1
            curr = max(pick,notpick)
            prev2 = prev1
            prev1 = curr
        return prev1