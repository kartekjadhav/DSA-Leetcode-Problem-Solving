#TC - O(N), SC - O(1)
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        #Code here
        maxi = arr[n-1]
        ans = [maxi]
        
        for i in range(n-2, -1, -1):
            if arr[i]>=maxi: 
                ans.append(arr[i])
                maxi = arr[i]
        return ans[::-1]