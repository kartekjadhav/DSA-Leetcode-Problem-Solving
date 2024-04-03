#1. Top Down approach (Recursion) 

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

#2. Bottom Up Approach (Iterative)

#TC - O(N)
#SC - O(1)

#USING ARRAY FOR STORAGE (SC - O(N))
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[0],dp[1] = 1,1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
    
#Without Using Array (SC - O(1))
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,1
        for i in range(2,n+1):
            temp = b
            b = a + b
            a = temp
        return b
