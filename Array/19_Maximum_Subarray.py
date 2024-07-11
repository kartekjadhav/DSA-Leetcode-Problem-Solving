#TC - O(N), SC - O(1)
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxi = float('-inf')
        for i in range(len(nums)):
            currSum+=nums[i]
            maxi = max(maxi, currSum)
            if currSum<0: currSum = 0
        return maxi