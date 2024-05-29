#This question is followup of Frog_Jump.py
#NOTE - WE CAN SPACE OPTIMIZE IN THIS QUESTION. WE CAN FROM O(N) TO O(K) BUT IF K==N THEN IT WONT MAKE ANY SENSE TO SPACE OPTIMIZE
#TC - O(N), SC - O(N)
class Solution:
    def minimizeCost(self, height, n, k):
        dp = [0]*n
        dp[0] = 0
        for i in range(1,n):
            maxi = float("inf")
            for j in range(1,k+1):
                if i-j<0: break
                maxi = min(maxi,abs(height[i]-height[i-j]) + dp[i-j])
            dp[i] = maxi
        return dp[n-1]