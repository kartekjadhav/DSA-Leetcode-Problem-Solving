from typing import List
class Solution:
    #Recursion
    #TC - O(2^N), SC - extra space - O(1), stack space - O(N)
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(ind, buy):
            #Base Case
            if ind==n: return 0

            profit = 0
            if buy:
                profit = max(-prices[ind] + dfs(ind+1, 0), dfs(ind+1, 1))
            else:
                profit = max(prices[ind] + dfs(ind+1, 1), dfs(ind+1, 0))
            return profit
        
        n = len(prices)
        return dfs(0, 1)
    
    #Memorization
    #TC - O(N*2), SC - extra space - O(N*2), stack space - O(N)
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(ind, buy):
            #Base Case
            if ind==n: return 0
            if dp[ind][buy]!=-1: return dp[ind][buy]

            profit = 0
            if buy:
                profit = max(-prices[ind] + dfs(ind+1, 0), dfs(ind+1, 1))
            else:
                profit = max(prices[ind] + dfs(ind+1, 1), dfs(ind+1, 0))
            dp[ind][buy] = profit
            return dp[ind][buy]
        
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]
        return dfs(0, 1)
    
    #Tabulation
    #TC - O(N*2), SC - extra space - O(N*2), stack space - O(1)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n+1)]

        #Base Case
        dp[n][0] = 0
        dp[n][1] = 0

        for ind in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[ind] + dp[ind+1][0], dp[ind+1][1])
                else:
                    profit = max(prices[ind] + dp[ind+1][1], dp[ind+1][0])
                dp[ind][buy] = profit

        return dp[0][1]
    
    #Tabulation with space optimization
    #TC - O(N*2), SC - extra space - O(2*2), stack space - O(1)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prev = [0]*2
        curr = [0]*2

        for ind in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[ind] + prev[0], prev[1])
                else:
                    profit = max(prices[ind] + prev[1], prev[0])
                curr[buy] = profit
            prev = curr[:]

        return prev[1]
    
    #Tabulation with space optimization(using only 4 variables)
    #TC - O(N*2), SC - extra space - O(2*2), stack space - O(1)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prevBuy, prevSell = 0, 0

        for ind in range(n-1, -1, -1):
            currBuy, currSell = 0, 0
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[ind] + prevSell, prevBuy)
                else:
                    profit = max(prices[ind] + prevBuy, prevSell)
                if buy: currBuy = profit
                else: currSell = profit
            prevBuy = currBuy
            prevSell = currSell

        return prevBuy