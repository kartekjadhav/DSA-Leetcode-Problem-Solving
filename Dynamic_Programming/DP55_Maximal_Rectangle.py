# Time Complexity: O(N * (M+M)), where N = total no. of rows and M = total no. of columns.
# Reason: O(N) for running a loop to check all rows. Now, inside that loop, O(M) is for visiting all the columns, and another O(M) is for the function we are using. The function takes linear time complexity. Here, the size of the height array is M, so it will take O(M).

# Space Complexity: O(M), where M = total no. of columns.
# Reason: We are using a height array and a stack of size M.

from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def findArea(histogram):
            n = len(histogram)
            leftmin = [-1]*n
            rightmin = [n]*n

            #Rightmin
            stack = [0]
            for i in range(1, n):
                while stack and histogram[stack[-1]]>histogram[i]:
                    rightmin[stack.pop()] = i
                stack.append(i)
            
            #Leftmin
            stack = [n-1]
            for i in range(n-2, -1, -1):
                while stack and histogram[stack[-1]]>histogram[i]:
                    leftmin[stack.pop()] = i
                stack.append(i)
            
            ans = 0
            for i in range(n):
                res = histogram[i]*((rightmin[i]-1) - (leftmin[i]+1) + 1)
                ans = max(ans, res)
            return ans

        
        m, n = len(matrix), len(matrix[0])
        dp = [0]*n
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[j] += 1
                else:
                    dp[j] = 0
            maxArea = max(maxArea, findArea(dp))
        return maxArea