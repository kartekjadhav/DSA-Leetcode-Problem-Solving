class Solution:
    #Recursion
    #TC - O(Exponential), SC - extra space - O(1), stack space - O(N+M)
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(ind1, ind2):
            #Base Case
            if ind2<0: return 1
            if ind1<0: return 0

            #If same
            if s[ind1]==t[ind2]:
                return dfs(ind1-1, ind2-1) + dfs(ind1-1, ind2)
            #If not same
            return dfs(ind1-1, ind2)
        
        m,n = len(s), len(t)
        return dfs(m-1, n-1)
    
    #Memorization
    #TC - O(N*M), SC - extra space - O(N*M), stack space - O(N+M)
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(ind1, ind2):
            #Base Case
            if ind2<0: return 1
            if ind1<0: return 0
            if dp[ind1][ind2]!=-1: return dp[ind1][ind2]

            ans = 0
            #If same
            if s[ind1]==t[ind2]:
                ans = dfs(ind1-1, ind2-1) + dfs(ind1-1, ind2)
            #If not same
            else:
                ans = dfs(ind1-1, ind2)
            dp[ind1][ind2] = ans
            return dp[ind1][ind2]
        
        m,n = len(s), len(t)
        dp = [[-1]*n for _ in range(m)]
        return dfs(m-1, n-1)

    #Memorization with index shifting
    #TC - O(N*M), SC - extra space - O(N*M), stack space - O(N+M)
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(ind1, ind2):
            #Base Case
            if ind2==0: return 1
            if ind1==0: return 0
            if dp[ind1][ind2]!=-1: return dp[ind1][ind2]

            ans = 0
            #If same
            if s[ind1-1]==t[ind2-1]:
                ans = dfs(ind1-1, ind2-1) + dfs(ind1-1, ind2)
            #If not same
            else:
                ans = dfs(ind1-1, ind2)
            dp[ind1][ind2] = ans
            return dp[ind1][ind2]
        
        m,n = len(s), len(t)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        return dfs(m, n)
    
    #Tabulation 
    #TC - O(N*M), SC - extra space - O(N*M), stack space - O(1)
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        dp = [[-1]*(n+1) for _ in range(m+1)]

        #Base Case
        for ind1 in range(m+1):
            dp[ind1][0] = 1
        for ind2 in range(1, n+1):
            dp[0][ind2] = 0
        
        for ind1 in range(1, m+1):
            for ind2 in range(1, n+1):
                ans = 0
                #If same
                if s[ind1-1]==t[ind2-1]:
                    ans = dp[ind1-1][ind2-1] + dp[ind1-1][ind2]
                #If not same
                else:
                    ans = dp[ind1-1][ind2]
                dp[ind1][ind2] = ans

        return dp[m][n]
    
    #Tabulation with space optimization
    #TC - O(N*M), SC - extra space - O(2*M), stack space - O(1)
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        prev = [0]*(n+1)
        prev[0] = 1
        curr = [0]*(n+1)
        for ind1 in range(1, m+1):
            curr[0] = 1 
            for ind2 in range(1, n+1):
                ans = 0
                #If same
                if s[ind1-1]==t[ind2-1]:
                    ans = prev[ind2-1] + prev[ind2]
                #If not same
                else:
                    ans = prev[ind2]
                curr[ind2] = ans
            prev = curr[:]

        return prev[n]