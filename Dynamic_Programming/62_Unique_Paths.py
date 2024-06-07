class Solution:
    
    #Using Normal Recursion
    #TC - O(2^(M*N)), SC - stack space - O(M+N), extra space - O(1)
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i, j):
            #Base Case
            if i==0 and j==0: return 1
            if i<0 or j<0: return 0

            up = dfs(i-1, j)
            left = dfs(i, j-1)
            return up + left
        
        return dfs(m-1, n-1)

    #Memorization
    #TC - O(M*N), SC - stack space - O(M+N), extra space - O(M*N)
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i, j):
            #Base Case
            if i==0 and j==0: return 1
            if i<0 or j<0: return 0
            if dp[i][j]!=-1: return dp[i][j]

            up = dfs(i-1, j)
            left = dfs(i, j-1)
            dp[i][j] = up + left
            return dp[i][j]
        
        dp = [[-1]*n for _ in range(m)]
        return dfs(m-1, n-1)
    
    #Tabulation
    #TC - O(M*N), SC - extra space - O(N*M)
    def uniquePaths(self, m: int, n: int) -> int:  
        dp = [[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0: dp[i][j] = 1
                else:
                    up, right = 0, 0
                    if i>0: up = dp[i-1][j]
                    if j>0: right = dp[i][j-1]
                    dp[i][j] = up + right 

        return dp[m-1][n-1]
    
    #Tabulation with space optimization
    #TC - O(M*N), SC - extra space - O(N)
    def uniquePaths(self, m: int, n: int) -> int:  
        prev = [0]*n 
        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if i==0: curr[j] = 1
                else:
                    up, right = 0, 0
                    if i>0: up = prev[j]
                    if j>0: right = curr[j-1]
                    curr[j] = up + right 
            prev = curr[:]

        return prev[-1]