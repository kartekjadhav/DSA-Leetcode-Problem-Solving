from typing import List


class Solution:
    
    def __init__(self):
        self.mod = 10**9 + 7
    
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        # code here
        
        total = sum(arr)
        if total-d<0: return 0
        if (total-d)%2!=0: return 0
        
        k = (total-d)//2
        
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