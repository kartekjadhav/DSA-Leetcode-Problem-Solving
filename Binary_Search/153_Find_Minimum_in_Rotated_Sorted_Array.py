#TC - O(logN), SC - O(1)
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start,end = 0,len(nums)-1
        while start<end:
            mid = start + (end-start)//2
            if nums[mid-1]>=nums[mid]<=nums[mid+1]:
                return nums[mid]
            if nums[mid]<=nums[end]:
                end = mid-1
            else:
                start = mid+1
        return nums[start]