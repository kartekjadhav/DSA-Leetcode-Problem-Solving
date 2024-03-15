#TC - K*LOG(N)
#SC - O(1)

from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)
            heapq.heappush(nums, -res)
        return sum(nums)