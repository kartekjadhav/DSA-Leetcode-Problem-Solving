class Solution:
    #Recursion
    #TC - O(2^N * 2^M), SC - extra space - O(1), stack space - O(N+M)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Base Case
        def dfs(ind1, ind2):
            if ind1<0 or ind2<0: return 0

            #If character at ind1 in text1 and ind2 at text2 is same
            if text1[ind1]==text2[ind2]:
                return 1 + dfs(ind1-1, ind2-1)

            #If character at ind1 in text1 and ind2 at text2 is NOT same
            return max(dfs(ind1-1, ind2), dfs(ind1, ind2-1))
        
        n, m = len(text1), len(text2)
        return dfs(n-1, m-1)
    
    #Memorization
    #TC - O(N*M), SC - extra space - O(N*M), stack space - O(N+M)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(ind1, ind2):
            #Base Case
            if ind1<0 or ind2<0: return 0
            if dp[ind1][ind2]!=-1: return dp[ind1][ind2]

            ans = 0
            #If character at ind1 in text1 and ind2 at text2 is same
            if text1[ind1]==text2[ind2]:
                ans = 1 + dfs(ind1-1, ind2-1)

            #If character at ind1 in text1 and ind2 at text2 is NOT same
            else:
                ans =  max(dfs(ind1-1, ind2), dfs(ind1, ind2-1))
            
            dp[ind1][ind2] = ans
            return dp[ind1][ind2]
        
        n, m = len(text1), len(text2)
        dp = [[-1]*m for _ in range(n)]
        return dfs(n-1, m-1)
    
    #Memorization with index shifting
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(ind1, ind2):
            #Base Case
            if ind1==0 or ind2==0: return 0
            if dp[ind1][ind2]!=-1: return dp[ind1][ind2]

            ans = 0
            #If character at ind1 in text1 and ind2 at text2 is same
            if text1[ind1-1]==text2[ind2-1]:
                ans = 1 + dfs(ind1-1, ind2-1)

            #If character at ind1 in text1 and ind2 at text2 is NOT same
            else:
                ans =  max(dfs(ind1-1, ind2), dfs(ind1, ind2-1))
            
            dp[ind1][ind2] = ans
            return dp[ind1][ind2]
        
        n, m = len(text1), len(text2)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        return dfs(n, m)
    
    #Tabulation (Do this after index shifting)
    #TC - O(N*M), SC - extra space - O(N*M), stack space - O(1)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[-1]*(m+1) for _ in range(n+1)]

        #Base Case
        for ind1 in range(n+1):
            dp[ind1][0] = 0
        for ind2 in range(m+1):
            dp[0][ind2] = 0
        
        for ind1 in range(1, n+1):
            for ind2 in range(1, m+1):
                ans = 0
                #If character at ind1 in text1 and ind2 at text2 is same
                if text1[ind1-1]==text2[ind2-1]:
                    ans = 1 + dp[ind1-1][ind2-1]

                #If character at ind1 in text1 and ind2 at text2 is NOT same
                else:
                    ans =  max(dp[ind1-1][ind2], dp[ind1][ind2-1])
                
                dp[ind1][ind2] = ans

        return dp[n][m]
    
    #Tabulation with space optimization
    #TC - O(N*M), SC - extra space - O(1001), stack space - O(1)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        prev = [0]*1001
        curr = [0]*1001
        
        for ind1 in range(1, n+1):
            curr = [0]*1001
            for ind2 in range(1, m+1):
                ans = 0
                #If character at ind1 in text1 and ind2 at text2 is same
                if text1[ind1-1]==text2[ind2-1]:
                    ans = 1 + prev[ind2-1]

                #If character at ind1 in text1 and ind2 at text2 is NOT same
                else:
                    ans =  max(prev[ind2], curr[ind2-1])
                
                curr[ind2] = ans
            prev = curr

        return prev[m]