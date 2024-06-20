from typing import List
class Solution:
    #Recursion
    #TC - Exponential, SC - extra space - O(1), stack space - O(W)
    def knapSack(self, N, W, val, wt):
        # code here
        def dfs(ind, weight):
            if ind==0:
                items = weight//wt[0]
                return items*val[0]
            
            #not pick
            notpick = dfs(ind-1, weight)
            #pick
            pick = 0
            if weight>=wt[ind]: pick = val[ind] + dfs(ind, weight-wt[ind])
            
            return max(notpick, pick)
        
        return dfs(N-1, W)
    
#Memorization
#TC - O(N*W), SC - extra space - O(N*W), stack space - O(W)
def unboundedKnapsack(N: int, W: int, val: List[int], wt: List[int]) -> int:
    # write your code here
    def dfs(ind, weight):
            if ind==0:
                items = weight//wt[0]
                return items*val[0]
            if dp[ind][weight]!=-1: return dp[ind][weight]
            
            #not pick
            notpick = dfs(ind-1, weight)
            #pick
            pick = 0
            if weight>=wt[ind]: pick = val[ind] + dfs(ind, weight-wt[ind])
            
            dp[ind][weight] = max(notpick, pick)
            
            return dp[ind][weight]
        
        
    dp = [[-1]*(W+1) for _ in range(N)]
    return dfs(N-1, W)

#Tabulation
#TC - O(N*W), SC - extra space - O(N*W), stack space - O(1)
def knapSack(self, N, W, val, wt):
        
        dp = [[-1]*(W+1) for _ in range(N)]
        for weight in range(W+1):
            items = weight//wt[0]
            dp[0][weight] = items*val[0]
        
        for ind in range(1, N):
            for weight in range(W+1):
                #not pick
                notpick = dp[ind-1][weight]
                #pick
                pick = 0
                if weight>=wt[ind]: pick = val[ind] + dp[ind][weight-wt[ind]]
                
                dp[ind][weight] = max(notpick, pick)
        
        return dp[N-1][W]

#Tabulation
#TC - O(N*W), SC - extra space - O(2*W), stack space - O(1)
def knapSack(self, N, W, val, wt):
        
        prev = [-1]*(W+1)
        curr = [-1]*(W+1)
        
        for weight in range(W+1):
            items = weight//wt[0]
            prev[weight] = items*val[0]
        
        for ind in range(1, N):
            for weight in range(W+1):
                #not pick
                notpick = prev[weight]
                #pick
                pick = 0
                if weight>=wt[ind]: pick = val[ind] + curr[weight-wt[ind]]
                
                curr[weight] = max(notpick, pick)
            
            prev = curr[:]
        
        return prev[W]

#More space optimization
#TC - O(N*W), SC - extra space - O(W), stack space - O(1)
def knapSack(self, N, W, val, wt):
        curr = [-1]*(W+1)
        
        for weight in range(W+1):
            items = weight//wt[0]
            curr[weight] = items*val[0]
        
        for ind in range(1, N):
            for weight in range(W+1):
                #not pick
                notpick = curr[weight]
                #pick
                pick = 0
                if weight>=wt[ind]: pick = val[ind] + curr[weight-wt[ind]]
                
                curr[weight] = max(notpick, pick)
        
        return curr[W]
