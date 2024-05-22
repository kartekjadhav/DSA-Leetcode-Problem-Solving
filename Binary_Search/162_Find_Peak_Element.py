#TC - O(logN), SC - O(1)
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start,end = 0,len(nums)-1
        while start<end:
            mid = start + (end-start)//2
            if nums[mid]<nums[mid+1]:
                start = mid+1
            else:
                end = mid
        return start