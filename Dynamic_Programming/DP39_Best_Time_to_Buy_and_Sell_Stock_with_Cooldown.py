from typing import List
class Solution:
    #TC - O(N*2), SC - extra space - O(N*2), stack space - O(1)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n+2)]

        for ind in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[ind] + dp[ind+1][0], dp[ind+1][1])
                else:
                    profit = max(prices[ind] + dp[ind+2][1], dp[ind+1][0])
                dp[ind][buy] = profit

        return dp[0][1]
    
    #Space optimization
    #TC - O(N*2), SC - extra space - O(3*2), stack space - O(1)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prev2 = [0]*2
        prev1 = [0]*2
        curr = [0]*2

        for ind in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[ind] + prev1[0], prev1[1])
                else:
                    profit = max(prices[ind] + prev2[1], prev1[0])
                curr[buy] = profit
            prev2 = prev1[:]
            prev1 = curr[:]

        return prev1[1]