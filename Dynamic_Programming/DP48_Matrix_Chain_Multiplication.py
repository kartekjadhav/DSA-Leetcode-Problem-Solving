class Solution:
    
    #Recursion
    #TC - Exponentially large, SC - extra space - O(1), stack space - O(N)
    def matrixMultiplication(self, n, arr):
        # code here
        def dfs(i, j):
            if i==j: return 0
            mini = float('inf')
            for k in range(i, j):
                res = dfs(i,k) + dfs(k+1,j) + arr[i-1]*arr[k]*arr[j]
                mini = min(mini, res)
            return mini
        
        return dfs(1, n-1)
    
    #Memorization
    #TC - O(N*N*N), SC - extra space - O(N*N), stack space - O(N)
    def matrixMultiplication(self, n, arr):
        # code here
        def dfs(i, j):
            #Base Case
            if i==j: return 0
            if dp[i][j]!=-1: return dp[i][j]
            
            mini = float('inf')
            for k in range(i, j):
                res = dfs(i,k) + dfs(k+1,j) + arr[i-1]*arr[k]*arr[j]
                mini = min(mini, res)
            dp[i][j] = mini
            return dp[i][j]
        
        dp = [[-1]*n for _ in range(n)]
        return dfs(1, n-1)

    #Tabulation
    #TC - O(N*N*N), SC - extra space - O(N*N), stack space - O(1)
    def matrixMultiplication(self, n, arr):
        # code here
        dp = [[-1]*n for _ in range(n)]
        #Base Case
        for i in range(n):
            dp[i][i] = 0
        
        for i in range(n-1, 0, -1):
            for j in range(i+1,n):
                mini = float('inf')
                for k in range(i, j):
                    res = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                    mini = min(mini, res)
                dp[i][j] = mini
        
        return dp[1][n-1]