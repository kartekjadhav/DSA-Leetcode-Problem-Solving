#TC - O(N^3) + O(NlogN), SC - O(N)
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]: continue
            for j in range(i+1, n-2):
                if j>i+1 and nums[j]==nums[j-1]: continue
                start, end, k = j+1, n-1, target-(nums[i]+nums[j])
                while start<end:
                    res = nums[start] + nums[end]
                    if res==k: 
                        ans.append([nums[i], nums[j], nums[start], nums[end]])
                        while start<n-1 and nums[start]==nums[start+1]: start+=1
                        while end>0 and nums[end]==nums[end-1]: end-=1
                        start+=1
                        end-=1
                    elif res>k:
                        end-=1
                    else:
                        start+=1
        return ans