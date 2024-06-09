from typing import List
class Solution:
    
    #Normal Recursion
    #TC - O(2^(M*N)), SC - extra space - O(1), stack space - O(M+N)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(i,j):
            #Base Case
            if i<0 or j<0: return 0
            if obstacleGrid[i][j] == 1: return 0
            if i==0 and j==0: return 1
            
            up = dfs(i-1, j)
            left = dfs(i, j-1)

            return up+left
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return dfs(m-1, n-1)
    
    #Memorization
    #TC - O(M*N), SC - extra space - O(M*N), stack space - O(M+N)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(i,j):
            #Base Case
            if i<0 or j<0: return 0
            if dp[i][j]!=-1: return dp[i][j]
            if obstacleGrid[i][j] == 1: return 0
            if i==0 and j==0: return 1
            
            up = dfs(i-1, j)
            left = dfs(i, j-1)
            dp[i][j] = up + left 
            
            return dp[i][j]
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1]*n for _ in range(m)]
        return dfs(m-1, n-1)
    
    #Tabulation
    #TC - O(M*N), SC - extra space - O(M*N)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        #If starting and ending point is obstacle return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1 : return 0

        dp = [[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1: dp[i][j] = 0
                elif i==0 and j==0: dp[0][0] = 1
                else:
                    up, left = 0, 0 
                    if i>0: up = dp[i-1][j]
                    if j>0: left = dp[i][j-1]
                    dp[i][j] = up + left

        return dp[m-1][n-1]
    
    #Tablulation with space optimization
    #TC - O(M*N), SC - extra space - O(N)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        #If starting and ending point is obstacle return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1 : return 0

        prev = [0]*n
        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if obstacleGrid[i][j] == 1: curr[j] = 0
                elif i==0 and j==0: curr[0] = 1
                else:
                    curr[j] = prev[j]
                    if j>0: curr[j] += curr[j-1]
                    
            prev = curr[:]

        return prev[-1]