#TC - O(N), SC - O(1)
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w = -1,-1
        n = len(nums)
        for i in range(n):
            if nums[i]==0:
                w+=1
                nums[i], nums[w] = nums[w], nums[i]
                r+=1
                nums[w], nums[r] = nums[r], nums[w]
            
            elif nums[i]==1:
                w+=1
                nums[i], nums[w] = nums[w], nums[i]