#1. Memorization
#TC - O(N), SC - Extra - O(N), Stack - O(N) 

def frogJump(n: int, heights: List[int]) -> int:
    def helper(i):
        if i==0: return 0
        if dp[i]!=-1: return dp[i]
        left = helper(i-1) + abs(heights[i]-heights[i-1])
        right = float("inf")
        if i>1:
            right = helper(i-2) + abs(heights[i]-heights[i-2])
        dp[i] = min(left,right) 
        return dp[i]


    # Write your code here.
    dp = [-1]*(n+1)
    dp[0] = 0
    return helper(n-1)
    
#2. Tabulation
#TC - O(N), SC - Extra - O(N)
def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    dp = [-1]*(n)
    dp[0] = 0

    for i in range(1,n):
        jump1 = dp[i-1] + abs(heights[i]-heights[i-1])
        jump2 = float("inf")
        if i>1:
            jump2 = dp[i-2] + abs(heights[i]-heights[i-2])
        dp[i] = min(jump1,jump2)
    
    return dp[n-1]

#3. Tabulation
#TC - O(N), SC - Extra - O(1)

def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    dp = [-1]*(n+1)
    dp[0] = 0

    for i in range(1,n):
        jump1 = dp[i-1] + abs(heights[i]-heights[i-1])
        jump2 = float("inf")
        if i>1:
            jump2 = dp[i-2] + abs(heights[i]-heights[i-2])
        dp[i] = min(jump1,jump2)
    
    return dp[n-1]