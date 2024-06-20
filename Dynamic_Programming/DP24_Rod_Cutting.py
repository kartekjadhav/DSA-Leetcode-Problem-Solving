class Solution:
    
    #Recursion
    #TC - Exponential, SC - extra space - O(1), stack space - O(n)
    def cutRod(self, price, n):
        #code here
        def dfs(ind, L):
            if ind==0:
                return L*price[0]
            
            #not pick
            notpick = dfs(ind-1, L)
            #pick
            pick = float('-inf')
            if L>=ind+1: pick = price[ind] + dfs(ind, L - (ind+1))
            
            return max(notpick, pick)
        
        return dfs(n-1, n)
    
    #Memorization
    #TC - O(n*n), SC - extra space - O(n*n), stack space - O(n)
    def cutRod(self, price, n):
        #code here
        def dfs(ind, L):
            #Base Case
            if ind==0:
                return L*price[0]
            if dp[ind][L]!=-1: return dp[ind][L]
            
            #not pick
            notpick = dfs(ind-1, L)
            #pick
            pick = float('-inf')
            if L>=ind+1: pick = price[ind] + dfs(ind, L - (ind+1))
            
            dp[ind][L] = max(notpick, pick)
            
            return dp[ind][L]
        
        dp = [[-1]*(n+1) for _ in range(n)]
        return dfs(n-1, n)
    
    #Tabulation
    #TC - O(n*n), SC - extra space - O(n*n), stack space - O(1)
    def cutRod(self, price, n):
        #code here
        dp = [[-1]*(n+1) for _ in range(n)]
        for L in range(n+1):
            dp[0][L] = price[0]*L
        
        for ind in range(1, n):
            for L in range(n+1):
                #not pick
                notpick = dp[ind-1][L]
                #pick
                pick = float('-inf')
                if L>=ind+1: pick = price[ind] + dp[ind][L - (ind+1)]
                
                dp[ind][L] = max(notpick, pick)
        
        return dp[n-1][n]
    
    #Tabulation with space optimization
    #TC - O(n*n), SC - extra space - O(2*n), stack space - O(1)
    def cutRod(self, price, n):
        #code here
        prev = [-1]*(n+1)
        curr = [-1]*(n+1)
        
        for L in range(n+1):
            prev[L] = price[0]*L
        
        for ind in range(1, n):
            for L in range(n+1):
                #not pick
                notpick = prev[L]
                #pick
                pick = float('-inf')
                if L>=ind+1: pick = price[ind] + curr[L - (ind+1)]
                
                curr[L] = max(notpick, pick)
            
            prev = curr[:]
        
        return prev[n]
    
    #Tabulation with more space optimization
    #TC - O(n*n), SC - extra space - O(2*n), stack space - O(1)
    def cutRod(price, n):
    # Write your code here.
        curr = [-1]*(n+1)
        
        for L in range(n+1):
            curr[L] = price[0]*L
        
        for ind in range(1, n):
            for L in range(n+1):
                #not pick
                notpick = curr[L]
                #pick
                pick = float('-inf')
                if L>=ind+1: pick = price[ind] + curr[L - (ind+1)]
                
                curr[L] = max(notpick, pick)
            
            prev = curr[:]
        
        return prev[n]