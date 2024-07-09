#TC - O(N*N), SC - extra space - O(N), stack space - O(1)
from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def compareStrings(str1, str2):
            if len(str1)!=len(str2)+1: return False
            i, j = 0,0
            while i<len(str1) and j<len(str2):
                if str1[i]==str2[j]:
                    j+=1
                i+=1
            return j==len(str2)
        
        n = len(words)
        words.sort(key=lambda x: len(x))
        dp = [1]*n
        maxi = 1
        for ind in range(1, n):
            for prev_ind in range(ind):
                if compareStrings(words[ind], words[prev_ind]) and dp[prev_ind]+1 > dp[ind]:
                    dp[ind] = 1 + dp[prev_ind]
            maxi = max(maxi, dp[ind])
        return maxi