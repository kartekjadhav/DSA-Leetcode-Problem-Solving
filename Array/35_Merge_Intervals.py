#TC - O(NlogN), SC - O(N)
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x:x[0])
        ans = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            start, end = sorted_intervals[i]
            if start<=ans[-1][1]:
                if end>ans[-1][1]:
                    ans[-1][1] = end
            else:
                ans.append([start,end])
        return ans