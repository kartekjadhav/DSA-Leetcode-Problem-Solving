#TC - O(2^N)
#SC - EXTRA - O(N) , STACK SPACE - O(N)

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if i==len(nums):
                ans.append(ds[:])
                return
            ds.append(nums[i])
            helper(i+1)
            ds.pop()
            helper(i+1)

        ds = []
        ans = []
        helper(0)
        return ans