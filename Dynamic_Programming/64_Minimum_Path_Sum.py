from typing import List
class Solution:
    
    #Recursion
    #TC - O(2^(M*N)), SC - extra space - O(1), stack space - O(M+N)
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i<0 or j<0: return float("inf")
            if i==0 and j==0: return grid[0][0]

            up = dfs(i-1, j)
            left = dfs(i, j-1)

            return grid[i][j] + min(up, left)
        
        m, n = len(grid), len(grid[0])
        return dfs(m-1, n-1)
    
    #Memorization
    #TC - O(M*N), SC - extra spce - O(M*N), stack space - O(M+N)
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            #Base Cases
            if i<0 or j<0: return float("inf")
            if dp[i][j]!=-1: return dp[i][j]
            if i==0 and j==0: return grid[0][0]

            up = dfs(i-1, j)
            left = dfs(i, j-1)
            dp[i][j] = grid[i][j] + min(up, left)
            return dp[i][j]

        m, n = len(grid), len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        return dfs(m-1, n-1)
    
    #Tabulation
    #TC - O(M*N), SC - O(M*N)
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[0][0] = grid[0][0]
                else:
                    up, left = float('inf'), float('inf')
                    if i>0: up = dp[i-1][j]
                    if j>0: left = dp[i][j-1]
                    dp[i][j] = grid[i][j] + min(up, left)

        return dp[m-1][n-1]
    
    #Tabulation with space optimization
    #TC - O(M*N), SC - O(N)
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = [float('inf')]*n
        
        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if i==0 and j==0:
                    curr[0] = grid[0][0]
                else:
                    left = float('inf')
                    up = prev[j]
                    if j>0: left = curr[j-1]
                    curr[j] = grid[i][j] + min(up, left)
            prev = curr[:]

        return prev[-1]