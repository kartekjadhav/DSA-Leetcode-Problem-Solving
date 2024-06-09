from typing import List
class Solution:
    
    #Recursion
    #X - N*(N+1)//2, where N is no. of cols in last row
    #M - len(triangle)
    #TC - O(2^(X)), SC - stack space - O(M), extra space - O(1)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dfs(i, j):
            #Base Case
            if i==len(triangle)-1:
                return triangle[i][j]
            
            down = dfs(i+1, j)
            diag = dfs(i+1, j+1)

            return triangle[i][j] + min(down, diag)
        
        return dfs(0, 0)
    
    #Memorization
    #M - No. of rows, N - No. of cols in last row
    #TC - O(M*N), SC - extra space - O(N*N), stack space - O(M)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dfs(i, j):
            #Base Case
            if i==len(triangle)-1:
                return triangle[i][j]
            if dp[i][j]!=-1: return dp[i][j]
            
            down = dfs(i+1, j)
            diag = dfs(i+1, j+1)
            dp[i][j] = triangle[i][j] + min(down, diag)

            return dp[i][j]

        n = len(triangle)
        dp = [[-1]*n for _ in range(n)]
        return dfs(0, 0)
    
    #Tabulation
    #TC - O(N*N), SC - extra space - O(N*N)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1]*n for _ in range(n)]

        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]
        
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]
    
    #Tabulation with space optimization
    #TC - O(N*N), SC - extra space - O(N)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        below = [i for i in triangle[-1]]
        
        for i in range(n-2, -1, -1):
            curr = [-1]*(i+1)
            for j in range(i+1):
                curr[j] = triangle[i][j] + min(below[j], below[j+1])
            below = curr

        return below[0]