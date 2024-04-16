#Memorization
#TC - O(N)
#SC - stack - O(N),extra - O(N)
class Solution:
    def fib(self, n: int) -> int:
        def helper(i): 
            if dp[i]!=-1: return dp[i]
            dp[i] = helper(i-1) + helper(i-2)
            return dp[i]
        
        if n<=1: return n
        dp = [-1]*(n+1)
        dp[0], dp[1] = 0,1
        helper(n)
        return dp[n]

#Tabulation

#TC - O(N)
#SC - extra - O(N)

class Solution:
    def fib(self, n: int) -> int:
        dp = [0,1]
        for i in range(2,n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]


#TC - O(N)
#SC - extra - O(1)

class Solution:
    def fib(self, n: int) -> int:
        if n<=1: return n
        prev_2,prev_1 = 0,1
        for i in range(2,n+1):
            curr = prev_2 + prev_1
            prev_2 = prev_1
            prev_1 = curr
        return prev_1 