#TC - O(NLOGN)
#SC - O(1)

from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        arr = sorted(nums)
        i = 0
        while k>0:
            arr[i] *= -1
            if i+1 < n and arr[i+1] < arr[i]:
                i+=1
            k-=1
        return sum(arr)