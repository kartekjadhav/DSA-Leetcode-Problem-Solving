class Solution:
    #Brute Fore
    #TC - O(N^2), SC - O(1)
    def pairWithMaxSum(self, arr, n):
        # Your code goes here
        maxi = float('-inf')
        for i in range(n-1):
            smallest, sec_smallest = min(arr[i], arr[i+1]), max(arr[i], arr[i+1])
            maxi = max(maxi, smallest + sec_smallest)
            for j in range(i+2,n):
                if arr[i]<smallest:
                    sec_smallest = smallest
                    smallest = arr[i]
                elif smallest<arr[i]<sec_smallest:
                    sec_smallest = arr[i]
                maxi = max(maxi, smallest + sec_smallest)
        return maxi
    
    #Optimized
    #TC - O(N), SC - O(1)
    def pairWithMaxSum(self, arr, n):
        # Your code goes here
        maxi = float('-inf')
        for i in range(1, n):
            maxi = max(maxi, arr[i-1]+arr[i])
        return maxi