#TC - O(N), SC - O(1)
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        pos, neg = nums[0],nums[0]
        for i in range(1,len(nums)):
            val = nums[i]
            curr_pos = max(val, pos*val, neg*val)
            curr_neg = min(val, pos*val, neg*val)
            pos, neg = curr_pos, curr_neg
            ans = max(ans,pos)
        return ans