from typing import List
class Solution:
    
    #Recursion
    #TC - Exponential (greater than 2^n), SC - extra space - O(1), stack space - O(amount)
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(ind, target):
            #Base Case
            if ind==0:
                if target%coins[0]==0: return 1
                else: return 0
            #not pick
            notpick = dfs(ind-1, target)
            #pick
            pick = 0
            if coins[ind]<=target: pick = dfs(ind, target - coins[ind])

            return (pick + notpick)

        n = len(coins)
        return dfs(n-1, amount)
    
    #Memorization
    #TC - O(N*amount), SC - extra space - O(N*amount), stack space - O(amount)
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(ind, target):
            #Base Case
            if ind==0:
                if target%coins[0]==0: return 1
                else: return 0
            if dp[ind][target]!=-1: return dp[ind][target]

            #not pick
            notpick = dfs(ind-1, target)
            #pick
            pick = 0
            if coins[ind]<=target: pick = dfs(ind, target - coins[ind])

            dp[ind][target] = pick + notpick
            return dp[ind][target]

        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        return dfs(n-1, amount)
    
    #Tabulation
    #TC - O(N*amount), SC - extra space - O(N*amount), stack space - O(1)
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]
        #Base Case
        for target in range(amount+1):
            if target%coins[0]==0:
                dp[0][target] = 1

        for ind in range(1, n):
            for target in range(0, amount+1):
                #not pick
                notpick = dp[ind-1][target]
                #pick
                pick = 0
                if coins[ind]<=target: pick = dp[ind][target - coins[ind]]

                dp[ind][target] = pick + notpick

        return dp[n-1][amount]
    
    #Tabulation with space optimization
    #TC - O(N*amount), SC - extra space - O(amount), stack space - O(1)
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        prev = [0]*(amount+1)
        curr = [0]*(amount+1)
        
        #Base Case
        for target in range(amount+1):
            if target%coins[0]==0:
                prev[target] = 1

        for ind in range(1, n):
            for target in range(0, amount+1):
                #not pick
                notpick = prev[target]
                #pick
                pick = 0
                if coins[ind]<=target: pick = curr[target - coins[ind]]

                curr[target] = pick + notpick
            prev = curr

        return prev[amount]