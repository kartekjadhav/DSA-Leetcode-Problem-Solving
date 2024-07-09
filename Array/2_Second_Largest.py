#TC - O(N), SC - O(1)
class Solution:
    def print2largest(self, arr):
        # Code Here
        maxi, s_maxi = arr[0], -1
        for i in range(1, len(arr)):
            if arr[i]>maxi:
                s_maxi = maxi
                maxi = arr[i]
            
            elif arr[i]>s_maxi and arr[i]!=maxi:
                s_maxi = arr[i]
        
        return s_maxi