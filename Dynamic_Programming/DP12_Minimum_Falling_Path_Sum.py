from typing import List
class Solution:
    
    #Recursion
    #TC - O(3^(M*N)), SC - extra space - O(1), stack space - O(N)
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            #Base Cases
            if j<0 or j>=len(matrix[0]): return float("inf")
            if i==len(matrix)-1: return matrix[i][j]

            downleft = matrix[i][j] + dfs(i+1, j-1)
            down = matrix[i][j] + dfs(i+1, j)
            downright = matrix[i][j] + dfs(i+1, j+1)

            return min(downleft, down, downright)
        
        ans = float('inf')
        for j in range(len(matrix[0])):
            ans = min(ans, dfs(0, j))
        
        return ans
    
    #Memorization
    #TC - O(M*N), SC - extra space - O(M*N), stack space - O(N)
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            #Base Cases
            if j<0 or j>=len(matrix[0]): return float("inf")
            if dp[i][j]!=-1: return dp[i][j]
            if i==len(matrix)-1: return matrix[i][j]

            downleft = matrix[i][j] + dfs(i+1, j-1)
            down = matrix[i][j] + dfs(i+1, j)
            downright = matrix[i][j] + dfs(i+1, j+1)

            dp[i][j] = min(downleft, down, downright)
            
            return dp[i][j] 
        
        m,n = len(matrix), len(matrix[0])
        dp = [[-1]*n for _ in range(m)]
        ans = float('inf')
        for j in range(n):
            ans = min(ans, dfs(0, j))
        
        return ans
    
    #Tabulation
    #TC - O(M*N), SC - extra space - O(M*N), stack space - O(1)
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [[-1]*n for _ in range(m)]
        
        for j in range(n):
            dp[m-1][j] = matrix[m-1][j]

        for r in range(m-2, -1, -1):
            for c in range(n):
                downleft, down, downright = float("inf"), float("inf"), float("inf")
                down = matrix[r][c] + dp[r+1][c]
                if c>0: downleft = matrix[r][c] + dp[r+1][c-1]
                if c<n-1: downright = matrix[r][c] + dp[r+1][c+1]
                dp[r][c] = min(down, downleft, downright)
        
        ans = float('inf')

        for j in range(n):
            ans = min(ans, dp[0][j])
        
        return ans
    
    #Tabulation with space optimization
    #TC - O(M*N), SC - extra space - O(N), stack space - O(1)
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        below = [val for val in matrix[m-1]]

        for r in range(m-2, -1, -1):
            curr = [-1]*n
            for c in range(n):
                downleft, down, downright = float("inf"), float("inf"), float("inf")
                down = matrix[r][c] + below[c]
                if c>0: downleft = matrix[r][c] + below[c-1]
                if c<n-1: downright = matrix[r][c] + below[c+1]
                curr[c] = min(down, downleft, downright)
            below = curr

        ans = float('inf')

        for j in range(n):
            ans = min(ans, below[j])
        
        return ans