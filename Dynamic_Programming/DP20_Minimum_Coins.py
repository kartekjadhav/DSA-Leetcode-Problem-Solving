from typing import List
class Solution:
    
    #Recursion
    #TC - Exponential (More than 2^n), SC - extra space - O(1), stack space - O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(ind, target):
            if ind==0:
                if target%coins[0] == 0: return target//coins[0]
                else: return float('inf')
            
            #notpick
            notpick = dfs(ind-1, target)
            #pick
            pick = float('inf')
            if coins[ind]<=target: pick =  1 + dfs(ind, target - coins[ind])

            return min(pick, notpick)
        
        n = len(coins)
        ans = dfs(n-1, amount)
        if ans==float('inf'): return -1
        return ans

    #Memorization
    #TC - O(N*amount), SC - extra space - O(N*amount), stack space - O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(ind, target):
            if ind==0:
                if target%coins[0] == 0: return target//coins[0]
                else: return float('inf')
            if dp[ind][target]!=-1: return dp[ind][target]

            #notpick
            notpick = dfs(ind-1, target)
            #pick
            pick = float('inf')
            if coins[ind]<=target: pick =  1 + dfs(ind, target - coins[ind])

            dp[ind][target] = min(pick, notpick)
            return dp[ind][target]
        
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        ans = dfs(n-1, amount)
        if ans==float('inf'): return -1
        return ans
    
    #Tabulation
    #TC - O(N*amount), SC - extra space - O(N*amount), stack space - O(1)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0: return 0

        n = len(coins)
        dp = [[float('inf')]*(amount+1) for _ in range(n)]
        
        #Base Case
        for target in range(amount+1):
            if target%coins[0]==0:
                dp[0][target] = target//coins[0]
            
        for ind in range(1, n):
            for target in range(amount+1):
                #notpick
                notpick = dp[ind-1][target]
                #pick
                pick = float('inf')
                if coins[ind]<=target: pick =  1 + dp[ind][target - coins[ind]]

                dp[ind][target] = min(pick, notpick)
        
        ans = dp[n-1][amount]
        if ans==float('inf'): return -1
        return ans
    
    #Tabulation with space optimization
    #TC - O(N*amount), SC - extra space - O(amount), stack space - O(1)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0: return 0

        n = len(coins)
        prev = [float('inf')]*(amount+1)
        curr = [float('inf')]*(amount+1)
        
        #Base Case
        for target in range(amount+1):
            if target%coins[0]==0:
                prev[target] = target//coins[0]
            
        for ind in range(1, n):
            for target in range(amount+1):
                #notpick
                notpick = prev[target]
                #pick
                pick = float('inf')
                if coins[ind]<=target: pick =  1 + curr[target - coins[ind]]

                curr[target] = min(pick, notpick)
            prev = curr

        ans = prev[amount]
        if ans==float('inf'): return -1
        return ans