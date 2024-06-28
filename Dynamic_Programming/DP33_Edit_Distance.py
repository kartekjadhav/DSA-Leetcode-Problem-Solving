class Solution:
    #Recursion
    #TC - O(Exponential), SC - extra space - O(1), stack space - O(N+M)
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(ind1, ind2):
            #Base Case
            if ind1<0 and ind2<0: return 0
            elif ind1<0: return ind2+1
            elif ind2<0: return ind1+1

            #If same
            if word1[ind1]==word2[ind2]:
                return dfs(ind1-1, ind2-1)
            #If not same   
            return 1 + min(dfs(ind1-1, ind2),dfs(ind1, ind2-1),dfs(ind1-1, ind2-1))
        
        m,n = len(word1), len(word2)
        return dfs(m-1, n-1)
    
    #Memorization
    #TC - O(N*M), SC - extra space  - O(N*M), stack space - O(N+M)
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(ind1, ind2):
            #Base Case
            if ind1<0 and ind2<0: return 0
            elif ind1<0: return ind2+1
            elif ind2<0: return ind1+1
            if dp[ind1][ind2]!=-1: return dp[ind1][ind2]

            ans = 0
            #If same
            if word1[ind1]==word2[ind2]:
                ans = dfs(ind1-1, ind2-1)
            #If not same
            else:   
                ans = 1 + min(dfs(ind1-1, ind2),dfs(ind1, ind2-1),dfs(ind1-1, ind2-1))
            dp[ind1][ind2] = ans
            return dp[ind1][ind2]

        m,n = len(word1), len(word2)
        dp = [[-1]*n for _ in range(m)]
        return dfs(m-1, n-1)
    
    #Memorization with index shifting
    #TC - O(N*M), SC - extra space  - O(N*M), stack space - O(N+M)
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(ind1, ind2):
            #Base Case
            if ind1==0 and ind2==0: return 0
            elif ind1==0: return ind2+1
            elif ind2==0: return ind1+1
            if dp[ind1][ind2]!=-1: return dp[ind1][ind2]

            ans = 0
            #If same
            if word1[ind1-1]==word2[ind2-1]:
                ans = dfs(ind1-1, ind2-1)
            #If not same
            else:   
                ans = 1 + min(dfs(ind1-1, ind2),dfs(ind1, ind2-1),dfs(ind1-1, ind2-1))
            dp[ind1][ind2] = ans
            return dp[ind1][ind2]

        m,n = len(word1), len(word2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        return dfs(m, n)