from typing import List
def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    
    # Recursion
    #TC - O(3^(M*N) * 3^(M*N) * 9), SC - extra space - O(1), stack space - O(N)
    def dfs(i, j1, j2):
        #Base Cases
        if j1<0 or j1>=len(grid[0]) or j2<0 or j2>=len(grid[0]):
            return 0
        if i==len(grid)-1:
            if j1==j2: return grid[i][j1]
            else: return grid[i][j1] + grid[i][j2]
        
        direction = [-1, 0, 1]
        maxi = float('-inf')
        for delj1 in range(3):
            newj1 = j1 + direction[delj1]
            for delj2 in range(3):
                newj2 = j2 + direction[delj2]
                if j1==j2:
                    maxi = max(maxi, grid[i][j1] + dfs(i+1, newj1, newj2))
                else:
                    maxi = max(maxi, grid[i][j1] + grid[i][j2] + dfs(i+1, newj1, newj2))
        
        return maxi
    
    return dfs(0, 0, len(grid[0])-1)

    #Memorization
    #TC - O(M*N*N), SC - extra space - O(M*N*N), stack space - O(N)
    def dfs(i, j1, j2):
        #Base Cases
        if j1<0 or j1>=len(grid[0]) or j2<0 or j2>=len(grid[0]):
            return 0
        if dp[i][j1][j2]!=-1: return dp[i][j1][j2] 
        if i==len(grid)-1:
            if j1==j2: return grid[i][j1]
            else: return grid[i][j1] + grid[i][j2]
        
        direction = [-1, 0, 1]
        maxi = float('-inf')
        for delj1 in range(3):
            newj1 = j1 + direction[delj1]
            for delj2 in range(3):
                newj2 = j2 + direction[delj2]
                if j1==j2:
                    maxi = max(maxi, grid[i][j1] + dfs(i+1, newj1, newj2))
                else:
                    maxi = max(maxi, grid[i][j1] + grid[i][j2] + dfs(i+1, newj1, newj2))
        dp[i][j1][j2] = maxi
        return dp[i][j1][j2]

        
    m,n = len(grid), len(grid[0])
    dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(m)]
    return dfs(0, 0, len(grid[0])-1)


    #Tabulation
    #TC - O(M*N*N*9), SC - extra space - O(M*N*N), stack space - O(1)
    def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(m)]

        #Base Case for tabulation
        for j1 in range(n):
            for j2 in range(n):
                if j1==j2: dp[m-1][j1][j2] = grid[m-1][j1]
                else: dp[m-1][j1][j2] = grid[m-1][j1] + grid[m-1][j2] 

        direction = [-1, 0, 1]

        for i in range(m-2, -1, -1):
            for j1 in range(n):
                for j2 in range(n):
                    maxi = float('-inf')
                    for delj1 in range(3):
                        newj1 = j1 + direction[delj1]
                        for delj2 in range(3):
                            val = 0
                            newj2 = j2 + direction[delj2]
                            if j1==j2:
                                val = grid[i][j1]
                            else:
                                val = grid[i][j1] + grid[i][j2]
                            if 0<=newj1<n and 0<=newj2<n:
                                val += dp[i+1][newj1][newj2]
                            else:
                                val += float('-inf')
                            
                            maxi = max(maxi, val)
                    dp[i][j1][j2] = maxi

        return dp[0][0][n-1]

'''
We always space optimize from - 
        1. 1D array -> 2 variables
        2. 2D array -> 1D array
        3. therefore here in 3D array -> 2D array
'''

#Tabulation with space optimization
#TC - O(M*N*N*9), SC - extra space - O(N*N), stack space - O(1)
def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    m,n = len(grid), len(grid[0])
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    #Base Case for tabulation
    for j1 in range(n):
        for j2 in range(n):
            if j1==j2: dp[j1][j2] = grid[m-1][j1]
            else: dp[j1][j2] = grid[m-1][j1] + grid[m-1][j2] 

    direction = [-1, 0, 1]

    for i in range(m-2, -1, -1):
        temp = [[-1 for _ in range(n)] for _ in range(n)]
        for j1 in range(n):
            for j2 in range(n):
                maxi = float('-inf')
                for delj1 in range(3):
                    newj1 = j1 + direction[delj1]
                    for delj2 in range(3):
                        val = 0
                        newj2 = j2 + direction[delj2]
                        if j1==j2:
                            val = grid[i][j1]
                        else:
                            val = grid[i][j1] + grid[i][j2]
                        if 0<=newj1<n and 0<=newj2<n:
                            val += dp[newj1][newj2]
                        else:
                            val += float('-inf')                     
                        maxi = max(maxi, val)
                temp[j1][j2] = maxi
        dp = temp

    return dp[0][n-1]