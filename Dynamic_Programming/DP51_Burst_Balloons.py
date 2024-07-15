from typing import List
class Solution:
    #Recusion
    #TC - Exponentially high, SC - extra space - O(1), stack psace - O(N) 
    def maxCoins(self, nums: List[int]) -> int:
        def dfs(i, j):
            if i>j: return 0
            maxi = float('-inf')
            for k in range(i, j+1):
                coins = nums[i-1]*nums[k]*nums[j+1] + dfs(i, k-1) + dfs(k+1, j)
                maxi = max(maxi, coins)
            return maxi

        nums = [1] + nums + [1]
        return dfs(1, len(nums)-2)
    
    #Memorization
    #TC - O(N*N), SC - extra space - O(N*N), stack space - O(N)
    def maxCoins(self, nums: List[int]) -> int:
        def dfs(i, j):
            #Base Case
            if i>j: return 0
            if dp[i][j]!=-1: return dp[i][j]
            
            maxi = float('-inf')
            for k in range(i, j+1):
                coins = nums[i-1]*nums[k]*nums[j+1] + dfs(i, k-1) + dfs(k+1, j)
                maxi = max(maxi, coins)
            dp[i][j] = maxi
            return dp[i][j]

        nums = [1] + nums + [1]
        dp = [[-1]*len(nums) for _ in range(len(nums))]
        return dfs(1, len(nums)-2)


    #Tabulation
    #TC - O(N*N), SC - extra space - O(N*N), stack space - O(1)
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0]*len(nums) for _ in range(len(nums))]
        
        for i in range( len(nums)-2, 0, -1):
            for j in range( 1, len(nums)-1):
                if i>j: continue
                maxi = float('-inf')
                for k in range(i, j+1):
                    coins = nums[i-1]*nums[k]*nums[j+1] + dp[i][k-1] + dp[k+1][j]
                    maxi = max(maxi, coins)
                dp[i][j] = maxi
        
        return dp[1][len(nums)-2]
