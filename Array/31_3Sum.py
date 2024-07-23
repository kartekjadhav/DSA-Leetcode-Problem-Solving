from typing import List
class Solution:
    
    #TC - O(N^3), SC - O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        hashset = set()
        nums.sort()
        for i in range(n-2):
            for j in range(i+1,n-1):
                temp = nums[i] + nums[j]
                for k in range(j+1, n):
                    if nums[k] == (-1*temp):
                        hashset.add((nums[i], nums[j], nums[k]))

        result = [list(arr) for arr in hashset]
        return result

    #TC - O(N^2) + O(nlogN), SC - O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]: continue
            start, end, k = i+1, n-1, -nums[i]
            while start<end:
                res = nums[start] + nums[end]
                if res==k: 
                    ans.append([nums[i], nums[start], nums[end]])
                    while start<n-1 and nums[start]==nums[start+1]: start+=1
                    while end>0 and nums[end]==nums[end-1]: end-=1
                    start+=1
                    end-=1
                elif res>k:
                    end-=1
                else:
                    start+=1
        return ans

