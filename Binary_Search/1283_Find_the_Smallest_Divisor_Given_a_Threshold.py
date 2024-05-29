#TC - O(N*logN), SC - O(1) 

import math
from typing import List
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def validate(divisor):
            total = 0
            for num in nums:
                total += math.ceil(num/divisor)
                if total>threshold: return False
            return True
        
        start, end = 1, max(nums)
        while start<=end:
            mid = start + (end-start)//2
            if validate(mid):
                end = mid-1
            else:
                start = mid+1
        return start