#TC - O(M*N), SC - extra space - O(M*N), stack space - O(1)
class Solution:
    def longestCommonSubstr(self, text1, text2, n, m):
        # code here
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
        
        maxi = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                maxi = max(maxi, dp[i][j])
        
        return maxi