#TC - O(NlogN), SC - O(1)
from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def validate(n):
            partition = 1
            curr = 0
            for i,val in enumerate(nums):
                curr += val
                if curr>n:
                    partition+=1
                    curr = val
            return partition<=k
        
        start, end = max(nums), sum(nums)
        while start<=end:
            mid = start + (end-start)//2
            if validate(mid):
                end = mid-1
            else:
                start = mid+1
        return start