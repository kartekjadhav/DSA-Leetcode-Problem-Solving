from typing import List

#TC - O(N*N), SC - O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n): 
            for j in range(i):
                if nums[i]+nums[j]==target: return [j,i]


#TC - O(N), SC - O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if target-nums[i] in hashmap: break
            hashmap[nums[i]] = i
            
        return [hashmap[target-nums[i]],i]