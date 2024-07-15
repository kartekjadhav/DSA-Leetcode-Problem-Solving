class Solution:
    #Recursion
    #TC - O(N*N*N), SC - extra space - O(1), stack space - O(N)
    def minCut(self, s: str) -> int:
        def isPallindrome(start, end):
            i, j = start, end
            while i<=j:
                if s[i]!=s[j]: return False
                i+=1
                j-=1
            return True
        
        def dfs(ind):
            #Base Case
            if ind==len(s): return 0

            mini = float('inf')
            for j in range(ind,len(s)):
                if isPallindrome(ind, j):
                    count = 1 + dfs(j+1)
                    mini = min(mini, count)
            return mini

        return dfs(0)-1
    
    #Memorization
    #TC - O(N*N*N), SC - extra space - O(N), stack space - O(1)
    def minCut(self, s: str) -> int:
        def isPallindrome(start, end):
            i, j = start, end
            while i<=j:
                if s[i]!=s[j]: return False
                i+=1
                j-=1
            return True
        
        def dfs(ind):
            #Base Case
            if ind==len(s): return 0
            if dp[ind]!=-1: return dp[ind]

            mini = float('inf')
            for j in range(ind,len(s)):
                if isPallindrome(ind, j):
                    count = 1 + dfs(j+1)
                    mini = min(mini, count)
            dp[ind] = mini
            return dp[ind]

        dp = [-1]*len(s)
        return dfs(0)-1
    
    #Tabulation
    #TC - O(N*N), SC - extra space - O(N), stack space - O(1)
    def minCut(self, s: str) -> int:
        def isPallindrome(string):
            return string==string[::-1]

        dp1 = [0 for _ in range(len(s)+1)]
        dp2 = [[-1]*len(s) for _ in range(len(s))]

        for ind in range(len(s)-1, -1, -1):
            mini = float('inf')
            for j in range(ind, len(s)):
                if isPallindrome(s[ind : j+1]):
                    count = 1 + dp1[j+1]
                    mini = min(mini, count)
            dp1[ind] = mini

        return dp1[0]-1