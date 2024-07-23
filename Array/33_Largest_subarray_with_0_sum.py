#TC - O(N), SC - O(N)
class Solution:
    def maxLen(self, n, arr):
        #Code here
        prefix = {}
        prefixSum = 0
        maxLength = 0
        for i in range(n):
            prefixSum += arr[i]
            if prefixSum==0: maxLength = i+1
            elif prefixSum in prefix:
                maxLength = max(maxLength, i-prefix[prefixSum])
            else:
                prefix[prefixSum] = i
        return maxLength