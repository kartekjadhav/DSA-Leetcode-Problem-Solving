#TC - O(N*logN), SC - O(1)
from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate(wt):
            total_days = 1
            curr_wt = 0
            for i,n in enumerate(weights):
                curr_wt += n
                if curr_wt>wt:
                    total_days += 1
                    curr_wt = n
            return total_days<=days
        
        start, end = max(weights), sum(weights)
        while start<=end:
            mid = start + (end-start)//2
            if validate(mid):
                end = mid-1 
            else:
                start = mid+1
        return start