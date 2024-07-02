from typing import List
class Solution:
    #Recursion
    #TC - O(2^N), SC - extra space - O(1), stack space - O(N+2*K)
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(ind, transaction):
            #Base Case
            if ind==n or transaction==2*k: return 0

            profit = 0
            #Sell
            if transaction%2:
                profit = max(prices[ind] + dfs(ind+1, transaction+1), dfs(ind+1, transaction))
            #Buy
            else:
                profit = max(-prices[ind] + dfs(ind+1, transaction+1), dfs(ind+1, transaction))
            
            return profit
        
        k = 2
        n = len(prices)
        return dfs(0, 0)
    
    #Memorization
    #TC - O(N*2*K), SC - extra space - O(N*2*K), stack space - O(N+2*K)
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(ind, transaction):
            #Base Case
            if ind==n or transaction==2*k: return 0
            if dp[ind][transaction]!=-1: return dp[ind][transaction] 
            profit = 0
            #Sell
            if transaction%2:
                profit = max(prices[ind] + dfs(ind+1, transaction+1), dfs(ind+1, transaction))
            #Buy
            else:
                profit = max(-prices[ind] + dfs(ind+1, transaction+1), dfs(ind+1, transaction))
            
            dp[ind][transaction] = profit
            return dp[ind][transaction]
        
        k = 2
        n = len(prices)
        dp = [[-1]*(2*k) for _ in range(n)]
        return dfs(0, 0)
    
    #Tabulation
    #TC - O(N*2*K), SC - extra space - O(N*2*K), stack space - O(1)
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        n = len(prices)
        dp = [[0]*(2*k+1) for _ in range(n+1)]

        for ind in range(n-1, -1, -1):
            for transaction in range(2*k):
                profit = 0
                #Sell
                if transaction%2:
                    profit = max(prices[ind] + dp[ind+1][transaction+1], dp[ind+1][transaction])
                #Buy
                else:
                    profit = max(-prices[ind] + dp[ind+1][transaction+1], dp[ind+1][transaction])
                
                dp[ind][transaction] = profit

        return dp[0][0]
    
    #Tabulation with space optimization
    #TC - O(N*2*K), SC - extra space - O(2*K), stack space - O(1)
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        n = len(prices)
        prev = [0]*(2*k+1)
        curr = [0]*(2*k+1)

        for ind in range(n-1, -1, -1):
            for transaction in range(2*k):
                profit = 0
                #Sell
                if transaction%2:
                    profit = max(prices[ind] + prev[transaction+1], prev[transaction])
                #Buy
                else:
                    profit = max(-prices[ind] + prev[transaction+1], prev[transaction])
                
                curr[transaction] = profit
            prev = curr[:]

        return prev[0]