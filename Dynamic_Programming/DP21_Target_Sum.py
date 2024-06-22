from typing import List
class Solution:
    #Recursion
    #TC - O(2^N), SC - extra space - O(1), stack space - O(S2)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(ind, s):
            if ind==0:
                if s==0: 
                    if nums[0]==0: return 2
                    else: return 1
                elif nums[0]==s: return 1
                else: return 0
            
            #not pick
            notpick = dfs(ind-1, s)
            #pick
            pick = 0
            if s>=nums[ind]: pick = dfs(ind-1, s-nums[ind])
            
            return (pick + notpick) 

        total = sum(nums)
        n = len(nums)
        if (total-target)%2: return 0
        s2 = (total-target)//2
        
        return dfs(n-1, s2)
    
    #Memorization
    #TC - O(N*S2), SC - extra space - O(s2*N), stack space - O(N)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(ind, s):
            if ind==0:
                if s==0: 
                    if nums[0]==0: return 2
                    else: return 1
                elif nums[0]==s: return 1
                else: return 0
            if (ind, s) in hashmap: return hashmap[(ind, s)]

            #not pick
            notpick = dfs(ind-1, s)
            #pick
            pick = 0
            if s>=nums[ind]: pick = dfs(ind-1, s-nums[ind])
            hashmap[(ind, s)] = pick + notpick
            return hashmap[(ind, s)]

        total = sum(nums)
        n = len(nums)
        if (total-target)%2: return 0
        s2 = (total-target)//2
        hashmap = {}
        return dfs(n-1, s2)
    
    
    