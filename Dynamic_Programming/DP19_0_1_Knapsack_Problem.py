class Solution:
    
    #Recursion
    #TC - O(2^N), SC - extra space - O(1), stack space - O(N)
    def knapSack(self,W, wt, val, n):
       
        # code here
        def dfs(ind, weight):
            #Base Case
            if ind==0:
                if wt[0]<=weight: return val[0]
                else: return 0
            
            #not pick
            notpick = dfs(ind-1, weight)
            #pick
            pick = float('-inf')
            if weight>=wt[ind]: pick = val[ind] + dfs(ind-1, weight - wt[ind])
            
            return max(notpick, pick)
        
        return dfs(n-1, W)
    
    #Memorization
    #TC - O(N*W), SC - extra space - O(N*W), stack space - O(N)
    def knapSack(self,W, wt, val, n):
       
        # code here
        def dfs(ind, weight):
            #Base Case
            if ind==0:
                if wt[0]<=weight: return val[0]
                else: return 0
            if dp[ind][weight]!=-1: return dp[ind][weight]
            
            #not pick
            notpick = dfs(ind-1, weight)
            #pick
            pick = float('-inf')
            if weight>=wt[ind]: pick = val[ind] + dfs(ind-1, weight - wt[ind])
            
            dp[ind][weight] = max(notpick, pick)
            return dp[ind][weight]
        
        dp = [[-1]*(W+1) for _ in range(n)]
        return dfs(n-1, W)
    
    #Tabulation
    #TC - O(N*W), SC - extra space - O(N*W), stack space - O(1)
    def knapSack(self,W, wt, val, n):
        dp = [[0]*(W+1) for _ in range(n)]
        
        for weight in range(W+1):
            if wt[0]<=weight:
                dp[0][weight] = val[0]
        
        for ind in range(1, n):
            for weight in range(W+1):
                #not pick
                notpick = dp[ind-1][weight]
                #pick
                pick = float('-inf')
                if weight>=wt[ind]: pick = val[ind] + dp[ind-1][weight - wt[ind]]
                
                dp[ind][weight] = max(notpick, pick)
        
        
        return dp[n-1][W]
    
    #Tabulation
    #TC - O(N*W), SC - extra space - O(2*W)=O(W), stack space - O(1)
    def knapSack(self,W, wt, val, n):
        prev = [0]*(W+1)
        curr = [0]*(W+1)
        
        for weight in range(W+1):
            if wt[0]<=weight:
                prev[weight] = val[0]
        
        for ind in range(1, n):
            for weight in range(W+1):
                #not pick
                notpick = prev[weight]
                #pick
                pick = float('-inf')
                if weight>=wt[ind]: pick = val[ind] + prev[weight - wt[ind]]
                
                curr[weight] = max(notpick, pick)
            prev = curr[:]
        
        
        return prev[W]
    
    #More space optimization
    #TC - O(N*W), SC - extra space - O(W), stack space - O(1)
    def knapSack(self,W, wt, val, n):
        prev = [0]*(W+1)
        
        for weight in range(W+1):
            if wt[0]<=weight:
                prev[weight] = val[0]
        
        for ind in range(1, n):
            for weight in range(W, -1, -1):
                #not pick
                notpick = prev[weight]
                #pick
                pick = float('-inf')
                if weight>=wt[ind]: pick = val[ind] + prev[weight - wt[ind]]
                
                prev[weight] = max(notpick, pick)
        
        return prev[W]