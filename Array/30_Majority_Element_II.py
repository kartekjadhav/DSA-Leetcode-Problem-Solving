#TC - O(N), SC - O(N)
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        ans = []
        n = len(nums)
        for i,val in enumerate(nums):
            hashmap[val] = 1 + hashmap.get(val,0)
            if hashmap[val] > n//3:
                if not ans or ans[0]!=val: 
                    ans.append(val)
            if len(ans)==2: break

        return ans
    
    #TC - O(N), SC - O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        val1, count1 = float('inf'), 0
        val2, count2 = float('inf'), 0

        for i in range(len(nums)):
            if count1 == 0 and nums[i] != val2:
                val1 = nums[i]
                count1 = 1
            elif count2 == 0 and nums[i] != val1:
                val2 = nums[i]
                count2 = 1
            elif nums[i] == val1:
                count1 += 1
            elif nums[i] == val2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for i in nums:
            if i == val1: 
                count1 += 1
            elif i==val2:
                count2 += 1
        
        ans = []
        if count1 > len(nums)//3: ans.append(val1)
        if count2 > len(nums)//3: ans.append(val2)
        return ans