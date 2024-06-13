class Solution:
    def isSubsetSum (self, n, nums, k):
        # code here 
        
        #Recursion
        #TC - O(2^N), SC - extra space - O(1), stack space - O(N)
        def dfs(ind, target):
            #Base Cases
            if target==0: return True
            if ind==0: return nums[0]==target

            notpick = dfs(ind-1, target)
            if notpick: return True
            pick = False
            if target>=nums[ind]: pick = dfs(ind-1, target-nums[ind])
            return pick
        
        return dfs(n-1, k)
    
    #Memmorization
    #TC - O(N*K), SC - extra space - O(N*K), stack space - O(N)
    def isSubsetSum (self, n, nums, k):
        def dfs(ind, target):
            #Base Cases
            if target==0: return True
            if ind==0: return nums[0]==target
            if dp[ind][target]!=-1: return dp[ind][target]

            notpick = dfs(ind-1, target)
            pick = False
            if target>=nums[ind]: pick = dfs(ind-1, target-nums[ind])
            dp[ind][target] = pick or notpick
            return dp[ind][target] 
        
        dp = [[-1 for _ in range(k+1)] for _ in range(n)]
        return dfs(n-1, k)

    #Tabulation
    #TC - O(N*K), SC - extra space - O(N*K), stack space - O(1)
    def isSubsetSum (self, n, nums, k):
        dp = [[False for _ in range(k+1)] for _ in range(n)]
        
        for i in range(n): dp[i][0] = True
        if nums[0]<=k: dp[0][nums[0]] = True
        
        for ind in range(1, n):
            for target in range(1, k+1):
                notpick = dp[ind-1][target]
                pick = False
                if target>=nums[ind]: pick = dp[ind-1][target-nums[ind]]
                dp[ind][target] = pick or notpick
        
        return dp[n-1][k]
    
    #Tabulation with space optimization
    #TC - O(N*K), SC - extra space - O(K), stack space - O(1)
    def isSubsetSum (self, n, nums, k):
        
        prev = [False for _ in range(k+1)]
        prev[0] = True
        if nums[0]<=k: prev[nums[0]] = True
        
        for ind in range(1, n):
            curr = [False for _ in range(k+1)]
            curr[0] = True
            for target in range(1, k+1):
                notpick = prev[target]
                pick = False
                if target>=nums[ind]: pick = prev[target-nums[ind]]
                curr[target] = pick or notpick
            
            prev = curr
        
        return prev[k]