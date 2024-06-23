class Solution:
    #Recursion
    #TC - O(2^N * 2^N), SC - extra space - O(1),stack space - O(N+N)
    def longestPalindromeSubseq(self, s: str) -> int:
        def dfs(ind1, ind2):
            if ind1==0 or ind2==0: return 0

            ans = 0
            if text1[ind1-1]==text2[ind2-1]:
                ans = 1 + dfs(ind1-1, ind2-1)
            else:
                ans = max(dfs(ind1-1, ind2), dfs(ind1, ind2-1))
            return ans
        
        text1 = s
        text2 = text1[::-1]
        n = len(s)
        return dfs(n, n)
    
    #Memorization
    #TC - O(N*N), SC - extra space - O(N*N), stack space - O(N+N)
    def longestPalindromeSubseq(self, s: str) -> int:
        def dfs(ind1, ind2):
            if ind1==0 or ind2==0: return 0
            if dp[ind1][ind2]!=-1: return dp[ind1][ind2]
            ans = 0
            if text1[ind1-1]==text2[ind2-1]:
                ans = 1 + dfs(ind1-1, ind2-1)
            else:
                ans = max(dfs(ind1-1, ind2), dfs(ind1, ind2-1))
            dp[ind1][ind2] = ans
            return dp[ind1][ind2]
        
        text1 = s
        text2 = text1[::-1]
        n = len(s)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        return dfs(n, n)
    
    #Tabulation
    #TC - O(N*N), SC - extra space - O(N*N), stack space - O(1)
    def longestPalindromeSubseq(self, s: str) -> int:
        text1 = s
        text2 = text1[::-1]
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]

        for ind1 in range(1, n+1):
            for ind2 in range(1, n+1):
                ans = 0
                if text1[ind1-1]==text2[ind2-1]:
                    ans = 1 + dp[ind1-1][ind2-1]
                else:
                    ans = max(dp[ind1-1][ind2], dp[ind1][ind2-1])
                dp[ind1][ind2] = ans

        return dp[n][n]
    
    #Tabulation
    #TC - O(N*N), SC - extra space - O(N*2), stack space - O(1)
    def longestPalindromeSubseq(self, s: str) -> int:
        text1 = s
        text2 = text1[::-1]
        n = len(s)
        prev = [0]*(n+1)
        for ind1 in range(1, n+1):
            curr = [0]*(n+1)
            for ind2 in range(1, n+1):
                ans = 0
                if text1[ind1-1]==text2[ind2-1]:
                    ans = 1 + prev[ind2-1]
                else:
                    ans = max(prev[ind2], curr[ind2-1])
                curr[ind2] = ans
            prev = curr

        return prev[n]