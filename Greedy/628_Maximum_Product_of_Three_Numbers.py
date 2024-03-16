# Solution 1
#TC - O(NLOGN)
#SC - O(1)

from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        arr = sorted(nums)
        return max(arr[0]*arr[1]*arr[-1], arr[-1]*arr[-2]*arr[-3])
    
# Solution 2
#TC - O(N)
#SC - O(1)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1,max2,max3 = float("-inf"), float("-inf"), float("-inf")
        min1, min2 = float("inf"), float("inf")

        for val in nums:
            if val>=max1:
                max3 = max2
                max2 = max1
                max1 = val
            elif val>=max2:
                max3 = max2
                max2 = val
            elif val>max3:
                max3 = val
            
            if val<min1:
                min2 = min1
                min1 = val
            elif val<min2:
                min2 = val
        print(min1,min2,max1,max2,max3)
        return max(min1*min2*max1 , max1*max2*max3)