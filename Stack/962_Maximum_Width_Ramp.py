#TC - O(N)
#SC - O(N)
from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]
        for i in range(1,len(nums)):
            if nums[stack[-1]]>nums[i]:
                stack.append(i)
        
        maxWidth = 0
        if not stack: return maxWidth
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i]:
                j = stack.pop()
                maxWidth = max(maxWidth,i-j)
        return maxWidth