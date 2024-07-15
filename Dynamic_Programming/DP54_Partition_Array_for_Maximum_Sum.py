from typing import List
class Solution:
    #Recursion
    #TC - Exponential, SC - extra space - O(1), stack space - O(N) 
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        def dfs(ind):
            #Base Case
            if ind==len(arr): return 0

            maxi = float('-inf')
            ans = float('-inf')
            i = ind
            while i<len(arr) and i<ind+k:
                maxi = max(maxi, arr[i])
                res = (i-ind+1)*maxi + dfs(i+1)
                ans = max(ans, res)
                i+=1
            return ans
        
        return dfs(0)

    #Memorization
    #TC - O(N*K), SC - extra space - O(N), stack space - O(N) 
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        def dfs(ind):
            #Base Case
            if ind==len(arr): return 0
            if dp[ind]!=-1: return dp[ind]

            maxi = float('-inf')
            ans = float('-inf')
            i = ind
            while i<len(arr) and i<ind+k:
                maxi = max(maxi, arr[i])
                res = (i-ind+1)*maxi + dfs(i+1)
                ans = max(ans, res)
                i+=1
            dp[ind] = ans
            return dp[ind]
        
        dp = [-1]*len(arr)
        return dfs(0)

    #Tabulation
    #TC - O(N*K), SC - extra space - O(N), stack space - O(1) 
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0]*(len(arr)+1)

        for ind in range(len(arr)-1, -1, -1):
            maxi = float('-inf')
            ans = float('-inf')
            i = ind
            while i<len(arr) and i<ind+k:
                maxi = max(maxi, arr[i])
                res = (i-ind+1)*maxi + dp[i+1]
                ans = max(ans, res)
                i+=1
            dp[ind] = ans

        return dp[0]
