from typing import List

#Without DP

def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    def dfs(day, prev):
        maxi = 0
        if day==0:
            for task in range(3):
                if task!=prev:
                    point = points[day][task]
                    maxi = max(maxi, point)
        
        else:
            for task in range(3):
                if task!=prev:
                    point = points[day][task] + dfs(day-1, task)
                    maxi = max(maxi, point)
        
        return maxi
    
    return dfs(n-1, 3)

#Memorization
#TC - O(N*4*3), SC - extra space - O(N*4), stack space - O(N)  
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    def dfs(day, prev):

        if dp[day][prev] != 0: return dp[day][prev]
        if day==0:
            for task in range(3):
                if task!=prev:
                    point = points[day][task]
                    dp[day][prev] = max(dp[day][prev], point)
        
        else:
            for task in range(3):
                if task!=prev:
                    point = points[day][task] + dfs(day-1, task)
                    dp[day][prev] = max(dp[day][prev], point)
        
        return dp[day][prev]
    
    dp = [[0]*4 for _ in range(n)]
    return dfs(n-1, 3)

#Tabulation 
#TC - O(N*12), SC - O(N*4)
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    
    dp = [[0]*4 for _ in range(n)]

    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        for last in range(4):
            for task in range(3):
                if task!=last:
                    point = points[day][task] + dp[day-1][task]
                    dp[day][last] = max(dp[day][last], point)

    return dp[n-1][3]

#Tabulation with space optimization
#TC - O(N*12), SC - O(4)

def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    
    prev = [0]*4

    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        temp = [0]*4
        for last in range(4):
            for task in range(3):
                if task!=last:
                    point = points[day][task] + prev[task]
                    temp[last] = max(temp[last], point)
        prev = temp[:]
    return prev[-1]