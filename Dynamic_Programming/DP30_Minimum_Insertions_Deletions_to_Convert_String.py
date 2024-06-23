#TC - O(N*M), SC - extra space - O(N*M), stack space - O(1)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for ind1 in range(1, n+1):
            for ind2 in range(1, m+1):
                ans = 0
                if word1[ind1-1]==word2[ind2-1]:
                    ans = 1 + dp[ind1-1][ind2-1]
                else:
                    ans = max(dp[ind1-1][ind2], dp[ind1][ind2-1])
                dp[ind1][ind2] = ans

        lcs = dp[n][m]
        deletion = n - lcs
        insertion = m - lcs
        total = deletion + insertion
        return total

    #TC - O(N*M), SC - extra space - O(M), stack space - O(1)
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        prev = [0]*(m+1)

        for ind1 in range(1, n+1):
            curr = [0]*(m+1)
            for ind2 in range(1, m+1):
                ans = 0
                if word1[ind1-1]==word2[ind2-1]:
                    ans = 1 + prev[ind2-1]
                else:
                    ans = max(prev[ind2], curr[ind2-1])
                curr[ind2] = ans
            prev = curr

        lcs = prev[m]
        deletion = n - lcs
        insertion = m - lcs
        total = deletion + insertion
        return total