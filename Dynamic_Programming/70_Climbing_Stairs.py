#TC - O(N)
#SC - Extra - O(N), Stack - O(N)

class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(i):
            if i==0: return 1
            if i<0: return 0
            if dp[i]!=-1: return dp[i]
            dp[i] = helper(i-1) + helper(i-2)
            return dp[i]
        dp = [-1]*(n+1)
        dp[0] = 1
        return helper(n)
        