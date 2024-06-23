#This code is taken from DP28_Longest_Palindromic_Subsequence and modified accordinly
#TC - O(N*N), SC - extra space - O(2*N), stack space - O(1)
class Solution:
    def minInsertions(self, s: str) -> int:
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

        lcs = prev[n]
        return n - lcs