#TC - O(N), SC - O(N)
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixmap = {0:1}
        count, prefixSum = 0,0
        for i in nums:
            prefixSum += i
            res = prefixSum - k
            if res in prefixmap:
                count += prefixmap[res]
            prefixmap[prefixSum] = 1 + prefixmap.get(prefixSum, 0)
        return count 