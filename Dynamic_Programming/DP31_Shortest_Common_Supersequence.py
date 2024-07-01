#TC - O(N*M) + O(N+M) + O(N+M), SC - O(N*M)

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def getSuperSequence(lcs: str):
            i,j = 0,0
            result = []
            for c in lcs:
                while i<m and str1[i]!=c:
                    result.append(str1[i])
                    i+=1
                
                while j<n and str2[j]!=c:
                    result.append(str2[j])
                    j+=1
                result.append(c)
                i+=1
                j+=1

            result += str1[i:] + str2[j:]
            return "".join(result)
                

        m,n = len(str1), len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for ind1 in range(m+1):
            dp[ind1][0] = 0

        for ind2 in range(n+1):
            dp[0][ind2] = 0
        
        for ind1 in range(1,m+1):
            for ind2 in range(1,n+1):
                ans = 0
                if str1[ind1-1]==str2[ind2-1]:
                    ans = 1 + dp[ind1-1][ind2-1]
                else:
                    ans = max(dp[ind1-1][ind2], dp[ind1][ind2-1])
                dp[ind1][ind2] = ans
            
        ds = []
        i,j = m,n
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                ds.append(str1[i-1])
                i-=1
                j-=1
            else:
                if dp[i-1][j]>dp[i][j-1]:
                    i-=1
                else:
                    j-=1
        
        lcs = "".join(reversed(ds))
        return getSuperSequence(lcs)