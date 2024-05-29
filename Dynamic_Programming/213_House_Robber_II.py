#This is follow up question of 198_House_Robber.py
#TABULATION
#TC - 2*O(N), SC - O(N)
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            n = len(arr)
            prev2,prev1 = 0,arr[0]
            for i in range(1,n):
                pick = arr[i]
                if i>1:
                    pick += prev2
                notpick = 0 + prev1
                curr = max(pick,notpick)
                prev2 = prev1
                prev1 = curr
            return prev1

        if len(nums)==1: return nums[0]
        arr1, arr2 = nums[:-1], nums[1:]
        return max(helper(arr1), helper(arr2))
