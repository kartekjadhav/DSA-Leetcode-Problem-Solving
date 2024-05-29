#TC - O(N*logN), SC - O(1)

from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def validate(day,m,k):
            total = 0
            curr_count = 0
            for i,n in enumerate(bloomDay):
                if n<=day:
                    curr_count += 1
                else:
                    curr_count = 0
                if curr_count==k:
                    total += 1
                    curr_count = 0
            return total>=m
        
        if m*k > len(bloomDay): return -1
        start, end = min(bloomDay), max(bloomDay)
        while start<=end:
            mid = start + (end-start)//2
            if validate(mid,m,k):
                end = mid-1
            else:
                start = mid+1
        return start