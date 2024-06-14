class Solution:

    def __init__(self):
        self.mod = 10**9 + 7

    #Recursion
    #TC - O(2^N), SC - extra space - O(1), stack space - O(N)
    def perfectSum(self, arr, n, k):
        # code here
        def dfs(ind, target):
            #Base Cases
            if ind==0:
                if arr[0]==0 and target==0: return 2
                if arr[0]==target or target==0: return 1
                else: return 0
            
            #not pick
            notpick = dfs(ind-1, target)
            #pick
            pick = 0
            if target>=arr[ind]: pick = dfs(ind-1, target-arr[ind])
            
            return (pick + notpick)%self.mod
        
        return dfs(n-1, k)

    #Memorization
    #TC - O(N*K), SC - extra space - O(N*K), stack space - O(N)
    def perfectSum(self, arr, n, k):
            # code here
        def dfs(ind, target):
            #Base Cases
            if ind==0:
                if arr[0]==0 and target==0: return 2
                if arr[0]==target or target==0: return 1
                else: return 0
            if dp[ind][target]!=-1: return dp[ind][target]
            
            #not pick
            notpick = dfs(ind-1, target)
            #pick
            pick = 0
            if target>=arr[ind]: pick = dfs(ind-1, target-arr[ind])
            
            dp[ind][target] = (pick + notpick)%self.mod
            return dp[ind][target]
        
        dp = [[-1]*(k+1) for _ in range(n)]
        return dfs(n-1, k)

    #Tabulation
    #TC - O(N*K), SC - extra space - O(N*M), stack space - O(1)
    def perfectSum(self, arr, n, k):
            
        dp = [[0]*(k+1) for _ in range(n)]
        
        if arr[0]==0: dp[0][0] = 2
        else: dp[0][0] = 1
        
        if arr[0]<=k and arr[0]!=0: dp[0][arr[0]] = 1
        
        for ind in range(1, n):
            for target in range(k+1):
                #not pick
                notpick = dp[ind-1][target]
                #pick
                pick = 0
                if target>=arr[ind]: pick = dp[ind-1][target-arr[ind]]
                
                dp[ind][target] = (pick + notpick)%self.mod
        
        return dp[n-1][k]

    #Tabulation with space optimization
    #TC - O(N*K), SC - extra space - O(K), stack space - O(1)
    def perfectSum(self, arr, n, k):
        
        prev = [0]*(k+1)
        
        if arr[0]==0: prev[0] = 2
        else: prev[0] = 1
        
        if arr[0]<=k and arr[0]!=0: prev[arr[0]] = 1
        
        for ind in range(1, n):
            curr = [0]*(k+1)
            for target in range(k+1):
                #not pick
                notpick = prev[target]
                #pick
                pick = 0
                if target>=arr[ind]: pick = prev[target-arr[ind]]
                
                curr[target] = (pick + notpick)%self.mod
            prev = curr
        
        return prev[k]
