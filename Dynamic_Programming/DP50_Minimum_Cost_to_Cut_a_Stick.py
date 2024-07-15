from typing import List
class Solution:
    #Recursion
    #TC - Exponentially high, SC - extra space - O(1), stack space - O(N)
    def minCost(self, n: int, cuts: List[int]) -> int:
        def dfs(i, j):
            if i>j: return 0
            mini = float('inf')
            for k in range(i, j+1):
                cost = cuts[j+1]-cuts[i-1] + dfs(i, k-1) + dfs(k+1, j)
                mini = min(mini, cost)
            return mini

        cuts.sort()
        cuts.append(n)
        cuts.insert(0, 0)
        return dfs(1, len(cuts)-2)
    
    #Memorization
    #TC - O(N*N*N), SC - extra space - O(N*N), stack space - O(N)
    def minCost(self, n: int, cuts: List[int]) -> int:
        def dfs(i, j):
            #Base Case
            if i>j: return 0
            if dp[i][j]!=-1: return dp[i][j]

            mini = float('inf')
            for k in range(i, j+1):
                cost = cuts[j+1] - cuts[i-1] + dfs(i, k-1) + dfs(k+1, j)
                mini = min(mini, cost)
            dp[i][j] = mini
            return dp[i][j]
        
        cuts.sort()
        cuts.insert(0, 0)
        cuts.append(n)
        c = len(cuts)
        dp = [[-1]*c for _ in range(c)]
        return dfs(1, len(cuts)-2)
    
    #Tabulation
    #TC - O(N*N*N), SC - extra space - O(N*N), stack space - O(1)
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts.insert(0, 0)
        cuts.append(n)
        c = len(cuts)
        dp = [[0]*(c) for _ in range(c)]
        for i in range(c-2, 0, -1):
            for j in range(1, c-1):
                if i>j: continue
                mini = float('inf')
                for k in range(i, j+1):
                    cost = cuts[j+1] - cuts[i-1] + dp[i][k-1] + dp[k+1][j]
                    mini = min(mini, cost)
                dp[i][j] = mini

        return dp[1][len(cuts)-2]
